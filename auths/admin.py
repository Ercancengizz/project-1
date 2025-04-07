from django.contrib import admin
from auths.models import Register
from auths.forms import RegisterForm

class Adminform(admin.ModelAdmin):
    form = RegisterForm
    list_display = ('username', 'email', 'password')
    search_fields = ('username', 'password')

admin.site.register(Register, Adminform)
