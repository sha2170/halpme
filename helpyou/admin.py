from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)
#@admin.signup(CustomUser)
class admin(admin.ModelAdmin):
    list_display = (
        'username',
        'password1',
        'password2',
        'fullname',
        'address',
        'detailed_address',
        'year',
        'month',
        'day',
        'phone_number',
        'email',
        #'register_dttm' 계정 생성시간
    )

# Register your models here.
