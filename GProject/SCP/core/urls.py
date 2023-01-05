from django.urls import path
from . import views

app_name ='core'
urlpatterns = [
    path('', views.home, name= 'home'),
    path('clubs_list/', views.clubs_list, name= 'clubs_list'),  # name is used in templates.
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_info, name= 'login'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('<slug:slug>', views.club_details, name='club_details'),
]


