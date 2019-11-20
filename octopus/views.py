import pexpect
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse,HttpResponse
from cmdb.models import Server,InvertoryPool
from  .utils.handle import Handlecommand


class AsyncDemoView(View):
    def get(self,request):
        return render(request,'octopus/async.html')
    def post(self,request):
      ret = request.POST.get('num')
      from .tasks import add
      task2 = add.delay(int(ret))
      print("。。。。。。。。。。。。。。。。。。。。。。。。。---------->>>")
      return JsonResponse({"task_id":task2.id})


class AnsiblleView(View):
    def get(self,request):
        return render(request,'octopus/ansible.html')
    def post(self,request):
        host = request.POST.get('host')
        module = request.POST.get('module')
        conn = request.POST.get('conn')
        arg = request.POST.get('args')
        # ansible2 = MyAnsiable2(inventory = '/root/Auth_CMDB/auth_cmdb/octopus/inventory/host',connection=conn,remote_user='root')
        # ansible2.run(hosts= host, module=module,args=arg)
        # res = ansible2.get_result() 
        from .tasks import  ansibleExec
        task2 = ansibleExec.delay(host,module,conn,arg)
        return JsonResponse({"task_id":task2.id})




class ConnectionView(View):
     def get(self,request):
         conninfo = Server.objects.filter(connection__user__isnull=False)
         return render(request,"octopus/connection.html",{"connection":conninfo})

     def post(self,request):
        server_id = request.POST.get("server_id")
        server = Server.objects.filter(id = server_id).first()
        ip = server.manage_ip
        user = server.connection.user
        pwd = server.connection.passwd
        port = server.connection.port
        shell_comm = "ssh-copy-id -p {port} {user}@{ip}".format(port=port,user=user,ip=ip)
        # print(shell_comm)
        child = pexpect.spawn(shell_comm)
        index = child.expect("yes/no","password",pexpect.EOF,pexpect.TIMEOUT)
        try:
            child.sendline("yes")
            child.expect("password")
            child.sendline(pwd)
            child.expect("added")
            # print ("已向%s上传公钥"%(server))
            server.connection.authed = True
            server.connection.save()
            return JsonResponse({"status": True})
        except Exception as e:
            print(e)
            return JsonResponse({"status": False})


class ExecCommView(View):
     def get(self,request):
         Invertory = InvertoryPool.objects.all()
         return render(request,"octopus/run.html",{"Invertorys":Invertory})

     def post(self,request):
        command = request.POST.get("command")
        from .tasks import test_ansible
        task1 = test_ansible.delay(command)
        return JsonResponse({'task_id':task1.id})


from celery.result import AsyncResult
class TaskResultView(View):
    """
    通过id获取结果
    """
    def get(self, request):
        task_id = self.request.GET.get("task_id")
        task_obj = AsyncResult(id=task_id)
        task_json = {
            "id": task_obj.id,
            "status": task_obj.status,
            "success": task_obj.successful(),
            "result": task_obj.result
        }
        return JsonResponse(task_json)


