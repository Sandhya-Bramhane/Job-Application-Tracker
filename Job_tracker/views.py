from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from App.models import app
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required
def Appform(request):
    if request.method == 'POST':
        SN = request.POST.get('Number')
        JR = request.POST.get('JobR')
        JL = request.POST.get('JobL')
        SO = request.POST.get('source')
        JT = request.POST.get('JobT')
        CO = request.POST.get('contact')
        EM = request.POST.get('email')
        PI = request.POST.get('phoneI')
        ST = request.POST.get('status')
        FI = request.POST.get('firstInt')
        FIS = request.POST.get('firstIntSta')
        SI = request.POST.get('secondInt')
        SIS = request.POST.get('secondIntSta')
        FII = request.POST.get('finalInt')
        FIIS = request.POST.get('finalIntSta')
        DJ = request.POST.get('datejoin')
        CT = request.POST.get('ctc')

        data = app(
               Number=SN,
               JobRole=JR,
               JobLoc=JL,
               Source=SO,
               JobTy=JT,
               Contact=CO,
               Email=EM,
               phone_interview=PI,
               status=ST,
               first_interview=FI,
               first_interview_status=FIS,
               second_interview=SI,
               second_interview_status=SIS,
               final_interview=FII,
               final_interview_status=FIIS,
               date_of_joining=DJ,
               ctc=CT
        )
        data.save()

    return render(request, 'App.html')

@login_required
def AppFormdata(request):
    data = app.objects.all()
    context = {'store': data
    }
    return render(request, 'AppData.html', context)

@login_required
def AppDataDelete(request):
    D = request.GET['Number']
    print("Number=", D)
    data = app.objects.get(Number=D)
    data.delete()
    return HttpResponseRedirect("/appformdata")

@login_required
def AppDataSendToChange(request):
    n1 = request.GET['Num']
    jr1 = request.GET['jr']
    jl1 = request.GET['jl']
    so1 = request.GET['so']
    jt1 = request.GET['jt']
    co1 = request.GET['co']
    em1 = request.GET['em']
    pi1 = request.GET['pi']
    st1 = request.GET['st']
    fi1 = request.GET['fi']
    fis1 = request.GET['fis']
    si1 = request.GET['si']
    sis1 = request.GET['sis']
    fii1 = request.GET['fii']
    fiis1 = request.GET['fiis']
    dj1 = request.GET['dj']
    cc1 = request.GET['cc']

    context = {
        'n1': n1,
        'jr1': jr1,
        'jl1': jl1,
        'so1': so1,
        'jt1': jt1,
        'co1': co1,
        'em1': em1,
        'pi1': pi1,
        'st1': st1,
        'fi1': fi1,
        'fis1': fis1,
        'si1': si1,
        'sis1': sis1,
        'fii1': fii1,
        'fiis1': fiis1,
        'dj1': dj1, 
        'cc1': cc1,
    }
    return render(request, "AppDataEdit.html", context)


@login_required
def AppDataEdit(request):
    Number = request.GET['Number']
    JobRole = request.GET['JobR']
    JobLoc = request.GET['JobL']
    Source = request.GET['source']
    JobTy = request.GET['JobT']
    Contact = request.GET['contact']
    Email = request.GET['email']
    phone_interview = request.GET['phoneI']
    status = request.GET['status']
    first_interview = request.GET['firstInt']
    first_interview_status = request.GET['firstIntSta']
    second_interview = request.GET['secondInt']
    second_interview_status = request.GET['secondIntSta']
    final_interview = request.GET['finalInt']
    final_interview_status = request.GET['finalIntSta']
    date_of_joining = request.GET['datejoin']
    ctc = request.GET['ctc']

    data = app.objects.get(Number=Number)
    data.JobRole = JobRole
    data.JobLoc = JobLoc
    data.Source = Source
    data.JobTy = JobTy
    data.Contact = Contact
    data.Email = Email
    data.phone_interview = phone_interview
    data.status = status
    data.first_interview = first_interview
    data.first_interview_status = first_interview_status
    data.second_interview = second_interview
    data.second_interview_status = second_interview_status
    data.final_interview = final_interview
    data.final_interview_status = final_interview_status
    data.date_of_joining = date_of_joining
    data.ctc = ctc
    data.save()
    return HttpResponseRedirect("/appformdata")

    

def Home(request):
    return render(request,"home.html")

def Signup(request):
    message = ""
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        passw = request.POST.get("password")
        Confpass = request.POST.get("confirm_password")
        
        if passw != Confpass:
            message = "Your password and confirm password are not the same!!"
        else:
            if User.objects.filter(username=uname).exists():
                message = "Username already exists!"
            elif User.objects.filter(email=email).exists():
                message = "Email already exists!"
            else:
                my_user = User.objects.create_user(username=uname, email=email, password=passw)
                my_user.save()
                return redirect("/login")
    
    return render(request, "signup.html", {"message": message})

def Login(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("appform")  
        else:
            message = "Username or Password is incorrect!!"
    return render(request, "login.html", {"message": message})

def Logout(request):
    logout(request)
    return redirect("login")
