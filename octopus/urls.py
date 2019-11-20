from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = "octopus"

urlpatterns = [
  path('connection/',views.ConnectionView.as_view(),name="connection"),
  path('run/',views.ExecCommView.as_view(),name="Invertorys"),
  path('get_task/', views.TaskResultView.as_view(), name='getTask'),
  #  path('async/', views.AsyncDemoView.as_view(), name='asyncDemo'),
  path('ansible/', views.AnsiblleView.as_view(), name='ansible'),

]