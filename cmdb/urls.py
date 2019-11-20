from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register(r'assets', views.AssetViewSet)
router.register(r'server', views.ServerViewSet)
router.register(r'treenode', views.TreenodeViewSet)


app_name="cmdb"
urlpatterns=[
  path('', include(router.urls)),
  path('assets-list/',TemplateView.as_view(template_name='cmdb/assets.html'),name="assets"),
  path('server-list/',TemplateView.as_view(template_name='cmdb/server.html'),name="server"),
  # path('assets-vue/',TemplateView.as_view(template_name='cmdb/vue.html'),name="vue"),
  path('assets-detail/',TemplateView.as_view(template_name='cmdb/assets_detail.html'),name="assetdetail"),
  path('assetsfilter/',views.AssetListView.as_view(),name="assetfilter"),
  path('assetsnodefilter/',views.AssetnodeView.as_view(),name="assetsnodefilter"),
  path('assetmodel/<pk>/',views.AssetmodelView.as_view()),
  path('server-detail/',views.ServerDListView.as_view(),name='serverdatil'),

]