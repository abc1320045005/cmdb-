from django.shortcuts import render
from rest_framework import viewsets,generics,mixins
from django.views.generic import DetailView,ListView

from .serializers import AssetSerializer,ServerSerializer,TreeNodeSerializer,IDCSerializer
from .models import Asset,Server,TreeNode,IDC
from .page import StandardResultsSetPagination

#资产表取数据
class AssetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    pagination_class=StandardResultsSetPagination


# 资产表过滤 通过id来过滤
class AssetListView(generics.ListAPIView):
    serializer_class = AssetSerializer
    def get_queryset(self):
        queryset = Asset.objects.all()
        id = self.request.query_params.get('id', None)
        if id:
            queryset = queryset.filter(id=id)
        return queryset


class AssetnodeView(generics.ListAPIView):
    serializer_class = AssetSerializer
    def get_queryset(self):
        queryset = Asset.objects.all()
        id = self.request.query_params.get('id', None)
        if id:
            queryset = queryset.filter(node__id=id)
        return queryset


class AssetmodelView(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
      queryset = Asset.objects.all()
      serializer_class = AssetSerializer

      def get(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)

      def put(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)

      def delete(self, request, *args, **kwargs):
          return self.destroy(request, *args, **kwargs)




# server表取数据
class ServerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    pagination_class=StandardResultsSetPagination
   

# class ServerDetailView(DetailView):
#      model = Server
#      context_object_name = "serverdatil"
#      template_name = "cmdb/server-detail.html"
class ServerDListView(ListView):
     context_object_name = "serverdatil"
     template_name = "cmdb/server-detail.html"
     def  get_queryset(self):
         node_id = self.request.GET.get("node_id")
         return Server.objects.filter(asset__node__id = node_id)

     


class TreenodeViewSet(viewsets.ModelViewSet):
    queryset =  TreeNode.objects.filter(node_upstream=None)
    serializer_class = TreeNodeSerializer


class IDCViewset(viewsets.ReadOnlyModelViewSet):
     queryset = IDC.objects.all()
     serializer_class = IDCSerializer