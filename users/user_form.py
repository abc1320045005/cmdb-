import re

from django import forms
from .models import UsersProfile

gender_choice=(
  ("1","男"),
  ("2","女"),
)
# 继承了forms.ModelForm 使用model对form进行表单验证就会变得简单，属性在model中已经写好了
class UserRegisterModelForm(forms.ModelForm):
    class Meta:
       # 这是要使用的model中的值
        model = UsersProfile
        #你要进行验证的字段 必须是fields这个变量
        fields = ['username','password','mobile']

        widgets= {
          #字段名称：小插件
          'gender':forms.RadioSelect(),
          #这里注释的会被写入到前端页面中 后端就不需要写多少了
          # 'username': forms.TextInput(attrs={'class':'form-control'}),
          # 'password': forms.PasswordInput(attrs={'class':'form-control'}),
          # 'mobile': forms.TextInput(attrs={'class':'form-control'}),
          # 'age':forms.TextInput(attrs={'class':'form-control'})
        }

    def clean_mobile(self):
        """
        验证手机 号是否合法
        :return: 合法的数据或者错误信息
        """
        mobile = self.cleaned_data['mobile']
        PRGEX_MOBILE = r'^1[358]\d{9}|^147\d{8}|^176\d{8}$'
        regex = re.compile(PRGEX_MOBILE)
        if regex.match(mobile):
            return mobile
        else:
          # 主动抛出异常让程序来接收
            raise forms.ValidationError(
                '无效的手机号',
                code='mobile_invalid'
            )








    