from django.shortcuts import render, redirect

from .models import District, Branch,Account


# Create your views here.
def index(request):
    distcontext = District.objects.all()
    return render(request,"index.html",{'district':distcontext})


def getdata(request):
    template_name = 'getdata.html'
    distcontext = District.objects.all()
    brnchcontext = Branch.objects.all()
    return render(request, template_name, {'district': distcontext, 'branch': brnchcontext})

def adddata(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone','')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        district = request.POST.get('district', '')
        branch = request.POST.get('branch', '')
        account = request.POST.get('account', '')
        s = request.POST.getlist("chk[]")
        data = ''
        for s1 in s:
            data = data + s1 + " ,"
        print(data)

        acc_detail = Account(firstname=firstname, lastname=lastname, email=email,phone=phone,age=age,gender=gender,address=address,address2=address2,district=district,branch=branch,account=account,material=data)
        acc_detail.save()




        return render(request,'application_submitted.html')
    return render(request, 'getdata.html')