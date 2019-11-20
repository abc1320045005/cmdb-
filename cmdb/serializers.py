from rest_framework import serializers
from .models import Asset,Server,TreeNode,IDC,Cabinet


class subsubTreeNodeSerializer(serializers.ModelSerializer):
    sub_node = serializers.SerializerMethodField()
    class Meta:
        model = TreeNode
        fields = "__all__"
    def get_sub_node(self, obj):
        return []


class subTreeNodeSerializer(serializers.ModelSerializer):
    sub_node = subsubTreeNodeSerializer(many=True)
    class Meta:
      model = TreeNode
      fields = "__all__"


class TreeNodeSerializer(serializers.ModelSerializer):
     sub_node = subTreeNodeSerializer(many=True)
     class Meta:
        model = TreeNode
        fields = "__all__"



class ServerSerializer(serializers.ModelSerializer):
   
    sub_asset_type = serializers.SerializerMethodField()       
    created_by = serializers.SerializerMethodField()
    class Meta:
        model = Server
        fields = "__all__"   
    def get_sub_asset_type(self,obj):
        return obj.get_sub_asset_type_display()
    def get_created_by(self,obj):
        return obj.get_created_by_display()


class IDCSerializer(serializers.ModelSerializer): 
    class Meta:
        model = IDC
        fields = "__all__" 


class CabinetSerializer(serializers.ModelSerializer):  
    idc = IDCSerializer()
    class Meta:
        model = Cabinet
        fields = "__all__" 


class AssetSerializer(serializers.ModelSerializer):
    node = TreeNodeSerializer()
    cabinet = CabinetSerializer()
    server = ServerSerializer()   # 这个是在server表中与asset形成了一对一关系  需要序列化一下
    device_type = serializers.SerializerMethodField()
    device_status = serializers.SerializerMethodField()
    class Meta:
        model = Asset
        fields = "__all__"     
    def get_device_type(self,obj):
        return obj.get_device_type_id_display()
    def get_device_status(self,obj):
        return obj.get_device_status_id_display()


