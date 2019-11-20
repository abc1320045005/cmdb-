from __future__ import absolute_import, unicode_literals
from celery import shared_task


from .utils.handle  import Handlecommand
from cmdb.models import InvertoryPool
from  .utils.ansible_api  import MyAnsiable2,ResultCallback

@shared_task
def test_ansible(command):
     Invertory = InvertoryPool.objects.all()
     handel = Handlecommand(command,Invertory)
     ret = handel.exec_comm()
    #  import time 
    #  time.sleep(10)
    #  print("执行中")
     return ret


@shared_task
def add(n):
    import time
    time.sleep(8)
    return n+10

@shared_task
def ansibleExec(host,module,conn,arg):
      ansible2 = MyAnsiable2(inventory = '/root/Auth_CMDB/auth_cmdb/octopus/inventory/host',connection=conn,remote_user='root')
      ansible2.run(hosts=host, module=module,args=arg)
      res = ansible2.get_result()
      return res 