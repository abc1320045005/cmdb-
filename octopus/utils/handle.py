import subprocess
from auth_cmdb.settings import INVENT_PATH as invent_path

class Handlecommand:
    res_msg={
        "status":False,
        "msg": '命令格式错误'
    }
    def __init__(self, command,Invertory):
        self.command = command
        self.invent_path = invent_path
        self.Invertory = Invertory
        self.command_tpl = "{} -i {} -{}"
        self.rewrite()
    
    def rewrite(self):
         tpl_group = '[{}]\n'
         tpl_ip = '{}\n'
         content_list = []
         for g in self.Invertory:
           content_list.append(tpl_group.format(g.group))
           for ip in g.serevr.all():
               content_list.append(tpl_ip.format(ip.manage_ip))
         with open(self.invent_path,'w',encoding="utf-8") as f:
           f.writelines(content_list)

    def checked(self):
         """检查输入命令格式是否正确"""
         ansib, arg = self.command.split('-',  1)
         self.command = self.command_tpl.format(ansib, self.invent_path, arg)
         return self.command

    def exec_comm(self):
        """ 执行命令函数 """
        comm = self.checked()
        if comm:
          status, ret = subprocess.getstatusoutput(comm)
          if status == 0:
            self.res_msg['status'] = True
          self.res_msg['msg'] = ret
        return self.res_msg