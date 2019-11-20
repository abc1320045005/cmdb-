import xadmin

from .models import Asset,Server,TreeNode,Tag,IDC,Cabinet,Connection,InvertoryPool,Variable2Group,Variable2Server
class AssetAdmin(object):
    list_display = ('device_type_id', 'device_status_id', 'cabinet', 'name', 'latest_date', 'create_at')
    list_filter = ('device_type_id', 'device_status_id', 'cabinet', 'name',  'latest_date', 'create_at')
    search_fields = ('device_type_id', 'device_status_id', 'cabinet', 'name',  'latest_date', 'create_at')


class ServerAdmin(object):
    list_display = ('asset', 'sub_asset_type',  'model', 'os_type', 'os_distribution', 'os_release')
    list_filter = ('asset', 'sub_asset_type',  'model', 'os_type', 'os_distribution', 'os_release')
    search_fields = ('asset', 'sub_asset_type',  'model', 'os_type', 'os_distribution', 'os_release')


class TreeNodeAdmin(object):
    list_display = ('node_name', 'node_upstream')
    list_filter = ('node_name', 'node_upstream')
    search_fields = ('node_name', 'node_upstream')


class TagAdmin(object):
    list_display = ('name', 'latest_date', 'create_at')
    list_filter = ('name', 'latest_date', 'create_at')
    search_fields = ('name', 'latest_date', 'create_at')


class IDCAdmin(object):
    list_display = ('name', 'addr', 'phone', 'latest_date', 'create_at')
    list_filter = ('name', 'addr', 'phone', 'latest_date', 'create_at')
    search_fields = ('name', 'addr', 'phone', 'latest_date', 'create_at')


class CabinetAdmin(object):
    list_display = ('name', 'idc', 'latest_date', 'create_at')
    list_filter = ('name', 'idc', 'latest_date', 'create_at')
    search_fields = ('name', 'idc', 'latest_date', 'create_at')


class ConnectionAdmin(object):
    list_display = ('user', 'passwd', 'port', 'authed')
    list_filter = ('user', 'passwd', 'port', 'authed')
    search_fields = ('user', 'passwd', 'port', 'authed')


class InvertoryPoolAdmin(object):
    list_display = ('group',)
    list_filter = ('group',)
    search_fields = ('group',)


class Variable2GroupAdmin(object):
    list_display = ('key', 'val')
    list_filter = ('key', 'val')
    search_fields = ('key', 'val')


class Variable2ServerAdmin(object):
    list_display = ('key', 'val')
    list_filter = ('key', 'val')
    search_fields = ('key', 'val')



xadmin.site.register(TreeNode, TreeNodeAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(Cabinet, CabinetAdmin)
xadmin.site.register(Asset, AssetAdmin)
xadmin.site.register(Server, ServerAdmin)
xadmin.site.register(Connection, ConnectionAdmin)
xadmin.site.register(InvertoryPool, InvertoryPoolAdmin)
xadmin.site.register(Variable2Group, Variable2GroupAdmin)
xadmin.site.register(Variable2Server, Variable2ServerAdmin)