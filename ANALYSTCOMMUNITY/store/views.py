from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json 
import datetime
from .models import *
import razorpay
from django.conf import settings
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Order, ShippingAddress
from django.contrib.auth import get_user_model
User= get_user_model()


def store(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def cart(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		try:
			cart = json.loads(request.COOKIES['cart'])
		except:
			cart = {}
		print('Cart:', cart)

		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

		for i in cart:
			try:
				cartItems += cart[i]["quantity"]

				product = Product.objects.get(id=i)
				total = (product.price * cart[i]["quantity"])

				order['get_cart_total'] += total
				order['get_cart_items'] += cart[i]["quantity"]

				item = {
			  		'product':{
						'id':product.id,
						'name':product.name,
						'plan':product.plan,
						'price':product.price,
						'imageURL':product.image.url,
						},
					'quantity':cart[i]['quantity'],
					'get_total':total,
					}
				items.append(item)

				if product.digital == False:
					order['shipping'] = True
			except:
				pass
	
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']
	
	client = razorpay.Client(auth = (settings.KEY, settings.SECRET))
	payment = client.order.create({'amount' : order.get_cart_total * 100, 'currency':'INR', 'payment_capture':1})
	order.razor_pay_order_id= payment['id']
	order.save()

	context = {'items':items, 'order':order, 'cartItems':cartItems, 'payment':payment}
	return render(request, 'store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:',action)
	print('productId:',productId)

	customer = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	if action == 'add':
		orderItem.quantity = (orderItem.quantity +1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity -1)
	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()
	return JsonResponse('Item was Added', safe=False) 

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)


	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id
		

		if total == order.get_cart_total:
			order.complete = True
		order.save()

	if order.shipping == True:
		if request.user.is_authenticated:
			customer = request.user
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		else:
			items = []
			order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
			cartItems = order['get_cart_items']

		client = razorpay.Client(auth = (settings.KEY, settings.SECRET))
		payment = client.order.create({'amount' : order.get_cart_total * 100, 'currency':'INR', 'payment_capture':1})
		pay=ShippingAddress.objects.create(
		customer=customer,
		order=order,
		business_name=data['shipping']['business_name'],
		business_email=data['shipping']['business_email'],
		business_address=data['shipping']['business_address'],
		business_file=data['shipping']['business_file'],
		name=data['shipping']['name'],
		email=data['shipping']['email'],
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		razor_pay_order_id= payment['id'],
		)
		pay.save()

	return JsonResponse('Payment Submited...', safe=False)


def check(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/check.html', context)


def generate_invoice_pdf(request):
    
    if not request.user.is_authenticated:
        return HttpResponse('User not authenticated', status=401)

    try:
    
        order = Order.objects.filter(customer=request.user, complete=True).latest('date_orderd')
    except Order.DoesNotExist:
        return HttpResponse('No complete order found for the user', status=404)

    try:
       
        shipping_address = ShippingAddress.objects.get(order=order)
    except ShippingAddress.DoesNotExist:
        return HttpResponse('Shipping address not found for the order', status=404)

    customer = order.customer

    context = {
        'order': order,
        'customer': customer,
        'shipping_address': shipping_address,
        'order_items': order.orderitem_set.all(),
    }

    html_content = render_to_string('invoice_template.html', context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order.id}.pdf"'

    pisa_status = pisa.CreatePDF(html_content, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    return response


def process(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)


	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		total = float(data['form']['total'])
		order.transaction_id = transaction_id
		

		if total == order.get_cart_total:
			order.complete = True
		order.save()

	if order.shipping == True:
		if request.user.is_authenticated:
			customer = request.user
			items = order.orderitem_set.all()
			cartItems = order.get_cart_items
		else:
			items = []
			order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
			cartItems = order['get_cart_items']

		pay=ShippingAddress.objects.create(
		customer=customer,
		order=order,
		business_name=data['shipping']['business_name'],
		business_email=data['shipping']['business_email'],
		business_address=data['shipping']['business_address'],
		business_file=data['shipping']['business_file'],
		name=data['shipping']['name'],
		email=data['shipping']['email'],
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		) 
		pay.save()


	return JsonResponse('Payment Submited...', safe=False)





