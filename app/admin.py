from django.contrib import admin
from app.models import CustomUser
from app.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email']


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
