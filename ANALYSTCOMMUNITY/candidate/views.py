from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from myanalyst.models import JobPost , CandidateApplications
from candidate.models import MyApplyList
from store.models import *
# Create your views here.

@login_required
def candidateHome(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    planposts = JobPost.objects.all()
    return render(request,'candidate/dashboradh.html',{'planposts':planposts ,'cartItems':cartItems})

@login_required
def applyPlan(request,id):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        business = request.POST.get('business')
        duration = request.POST.get('duration')
        yearOfExt = request.POST.get('yearOfExt')
        dataset = request.FILES.get('dataset')
        plan = JobPost.objects.get(id=id)
        if CandidateApplications.objects.filter(user=request.user,plan=plan).exists():
            return redirect('dash')
        CandidateApplications(user=request.user,plan=plan,duration=duration,yearOfExt=yearOfExt,dataset=dataset).save()
        return redirect('dash')
    return render(request,'candidate/apply.html',{'cartItems':cartItems})

@login_required
def myjoblist(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    planlist = MyApplyList.objects.filter(user=request.user)
    return render(request,'candidate/myjoblist.html',{'planlist':planlist, 'cartItems':cartItems})












