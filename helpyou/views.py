from django.shortcuts import render, redirect
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
#from .forms import UserCreationForm

from argon2 import PasswordHasher #패스워드 암호화 - 해시함수


def index(request):
    return render(
        request,
        'helpyou/index.html',
    )





@csrf_exempt
def signup (request):
    
    if request.method == 'GET':
        return render(request, 'helpyou/signup.html')

    elif request.method == 'POST':

        username = request.POST.get('username','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2', '')
        fullname = request.POST.get('fullname','')
        address = request.POST.get('address','')
        detailed_address = request.POST.get('detailed_address','')
        year = request.POST.get('year','')
        month = request.POST.get('month','')
        day = request.POST.get('day','')
        phone_number = request.POST.get('phone_number','')
        email = request.POST.get('email','')

        if(username and password1 and password2 and email) == '':
            return redirect('/signup/')
        elif password1 != password2:
            return redirect('/signup/')
        else:
            customuser = CustomUser(
                username = username,
                #password = password,
                password1 = PasswordHasher().hash(password1),
                password2 = PasswordHasher().hash(password2),
                fullname = fullname,
                address = address,
                detailed_address = detailed_address,
                year = year,
                month = month,
                day = day,
                phone_number = phone_number,
                email = email

            )
            customuser.save()

        return redirect('/login') #회원가입 성공했을 떄 로그인 페이지로 이동시키기 - ok

