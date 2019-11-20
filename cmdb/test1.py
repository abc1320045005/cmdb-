import  os, sys
# 获取到项目的根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 把项目的根目录放到 sys.path 中
sys.path.insert(0, PROJECT_ROOT)

# 设置环境变量
os.environ["DJANGO_SETTINGS_MODULE"] = 'auth_cmdb.settings'
import django
django.setup()

if __name__ == "__main__":
    from cmdb.models import InvertoryPool
    invs = InvertoryPool.objects.all()
    for inv in  invs:
       for var in inv.var_group.all():
           print(inv.group,var.key,var.val)
       for host in inv.serevr.all():
           for hvar in host.var_server.all():
               print(inv.group,hvar.key,hvar.val,host.manage_ip,host.host_name)


     
