from django.urls import path
from auths.views import Register_view, home, dashboard, login_view, logout_view

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('register/', Register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
