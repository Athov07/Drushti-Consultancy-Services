from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from myanalyst.models import JobPost , CandidateApplications , SelectCandidateJob 
from candidate.models import IsSortList
from store.models import*
# Create your views here.

@login_required
def AnalystHome(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    planposts = JobPost.objects.filter(user=request.user)

    print(planposts)
    return render(request,'analyst/analystdashbordh.html',{'planposts':planposts,'cartItems':cartItems})

@login_required
def AnalystCandidateDetails(request,id):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    if JobPost.objects.filter(id=id).exists():
        planposts = JobPost.objects.get(id=id)
        planapplys = CandidateApplications.objects.filter(plan=planposts)
        # print(jobapplys)
        selectedCandidate = SelectCandidateJob.objects.filter(plan=planposts)
        print(selectedCandidate)
        return render(request,'analyst/candidate.html',{'planapplys':planapplys,'planposts':planposts,'selectedCandidate':selectedCandidate,'cartItems':cartItems})
    else:
        return render('analystdash') 

@login_required
def postJobs(request):
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
        title = request.POST.get('title')
        address = request.POST.get('address')
        name = request.POST.get('name')
        amountLow = request.POST.get('amountLow')
        amountHigh = request.POST.get('amountHigh')
        lastDateToApply  = request.POST.get('lastDateToApply')

        planposts = JobPost(user=request.user,title=title,address=address,name=name,amountLow=amountLow,amountHigh=amountHigh,lastDateToApply=lastDateToApply)
        planposts.save()
        msg = "Plan Upload Done.."
        return render(request,'analyst/postjob.html',{'msg':msg})
    return render(request,'analyst/postjob.html',{'cartItems':cartItems})

def acceptApplication(request):
    if request.method == 'POST':
        candidateid = request.POST.get('candidateid')
        jobpostid = request.POST.get('jobpostid') 
        candidate = CandidateApplications.objects.get(id=candidateid) 
        planposts = JobPost.objects.get(id=jobpostid)
        if SelectCandidateJob.objects.filter(candidate=candidate).exists()==False:
            SelectCandidateJob(plan=planposts,candidate=candidate).save()
            IsSortList(user=candidate.user,plan=planposts).save()
        return redirect('/candidatedetails/'+str(jobpostid)+"/")
    return redirect('analystdash')