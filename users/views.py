from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView,LogoutView

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserlogoutView(LogoutView):
    next_page = '/'




from .user_form import UserRegisterModelForm
from .models import UsersProfile

# 继承FormView 用来处理form中的数据并进行清洗后传入到数据库中
class UserRegisterModelForm(FormView):
  #模版地址
     template_name = 'users/register.html'
     # 指定以下那个类 类中有要有所用的model
     form_class = UserRegisterModelForm
     #成功后的路由跳转到这里
     success_url = reverse_lazy('users:user_login')

     def form_valid(self, form):
        user = UsersProfile(**form.cleaned_data)
        # set_password就是把这个密码给设置成密文然后用save方法存库
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)


     def form_invalid(self, form):
        print("form-->", form)
        # 返回到父类中去进行form是否唯一
        return super().form_invalid(form)



