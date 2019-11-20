from django.urls import path

from . import views

app_name="users"

urlpatterns=[
  path('register/',views.UserRegisterModelForm.as_view(),name="usersRegister"),
  path('login/',views.UserLoginView.as_view(),name="user_login"),
   path('logout/',views.UserlogoutView.as_view(),name="logout"),
]