from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from .models import CustomUser
from argon2 import PasswordHasher, exceptions

     #회원가입 폼 클래스를 생성함과 동시에 forms의 ModelForm을 상속받음

class CustomUser(AbstractUser):




    field_order = [
        'username',
        #'username_check',
        'password1',
        'password2',
        #'fullname',
        'email'
    ]





    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'fullname','email')


    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username','')
        #username_check = cleaned_data.get('username_check','')
        password1 = cleaned_data.get('password1','')
        password2 = cleaned_data.get('password2','')
        #fullname = cleaned_data.get('fullname','')
        email = cleaned_data.get('email','')

        if password1 != password2:
            return self.add_error('password2', '비밀번호가 일치하지 않습니다.')
        elif 8 > len(password1):
            return self.add_error('password1', '비밀번호는 8자 이상으로 적어주세요.')
        else:
            self.username = username
            self.email = email




class SignupForm(forms.ModelForm):
    username = forms.CharField(
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'username',
                'placeholder' : '아이디'
            }
        ),
        error_messages={
            'required' : '아이디를 입력해주세요.',
            'unique' : '중복된 아이디입니다.'
        }
    )

#여기까지 회원가입 폼


#로그인폼

#class LoginForm(forms.Form):
    #username = forms.CharField(
        #max_length=32,
        #label='아이디',
        #required=True,
        #widget=forms.TextInput(
            #attrs={
                #'class' : 'username',
                #'placeholder' : '아이디'
            #}
        #),
        #error_messages={'required' : '아이디를 입력해주세요.'}
    #)
    #password1 = forms.CharField(
       # max_length=128,
        #label='비밀번호',
        #required=True,
        #widget=forms.PasswordInput(
          #  attrs={
          #      'class' : 'password1',
          #      'placeholder' : '비밀번호'
          #  }
        #),
        #error_messages={'required' : '비밀번호를 입력해주세요.'})


    #def clean(self):
     #   cleaned_data = super().clean()

      #  username = cleaned_data.get('username','')
      #  password1 = cleaned_data.get('password1','')

        #if username == '':
           # return self.add_error('username', '아이디를 다시 입력해주세요.')
        #elif password1 == '':
         #   return self.add_error('password1', '비밀번호를 다시 입력해주세요.')
        #else:
          ###except:
            #    try:
             #       customuser = CustomUser.objects.get(username=username)
             #   except CustomUser.DoesNotExist:
             #       return self.add_error('username','아이디가 존재하지 않습니다.')
             #   try:
             ##       PasswordHasher().verify(username, username)
               # except exceptions.VerifyMismatchError:
               #     return self.add_error('password1', '비밀번호가 다릅니다.')
