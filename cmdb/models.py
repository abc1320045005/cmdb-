from django.db import models
from django.utils import timezone

class TreeNode(models.Model):
    node_name = models.CharField('节点名称', max_length=128)
    node_upstream = models.ForeignKey('self',verbose_name='上级节点',
                                      related_name='sub_node',
                                      on_delete=models.CASCADE,
                                      blank=True,null=True)
    class Meta:
        verbose_name = "服务树节点表"
        verbose_name_plural = verbose_name
        db_table = 'tree_node'

    def __str__(self):
        up_node = self.node_upstream.node_name if self.node_upstream else '根节点'
        return f"{up_node}-->{self.node_name}"


class Tag(models.Model):
    name = models.CharField('标签', max_length=64)
    latest_date = models.DateField(verbose_name='更新时间', default=timezone.now, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = "标签信息表"
        verbose_name_plural = verbose_name
        db_table = 'tag'

    def __str__(self):
        return self.name


class IDC(models.Model):
    """
    IDC 机房信息
    """
    name = models.CharField('机房名称', max_length=128)
    addr = models.CharField('地址', max_length=256)
    phone = models.CharField('联系电话', max_length=11)
    latest_date = models.DateField(verbose_name='更新时间', default=timezone.now, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = "机房信息表"
        verbose_name_plural = verbose_name
        db_table = 'idc'

    def __str__(self):
        return self.name

class Cabinet(models.Model):
    """
    机柜信息
    """
    name = models.CharField("机柜编号", max_length=128)
    idc = models.ForeignKey('idc', related_name='cabinet',
                            verbose_name='所属机房',
                            on_delete=models.CASCADE)
    latest_date = models.DateField(verbose_name='更新时间', default=timezone.now, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = "机柜信息表"
        verbose_name_plural = verbose_name
        db_table = 'cabinet'

    def __str__(self):
        return self.name


class Asset(models.Model):
    """
    资产信息表，所有资产公共信息（交换机，服务器，防火墙等）
    """
    device_type_choices = (
        ('1', '服务器'),
        ('2', '路由器'),
        ('3', '交换机'),
        ('4', '防火墙'),
    )
    device_status_choices = (
        ('1', '上架'),
        ('2', '在线'),
        ('3', '离线'),
        ('4', '下架'),
    )

    device_type_id = models.CharField(choices=device_type_choices, max_length=1, default='1')
    device_status_id = models.CharField(choices=device_status_choices, max_length=1,default='1')
    cabinet = models.ForeignKey('cabinet',  verbose_name='所属机柜',
                                related_name='asset', on_delete=models.CASCADE)
    # cabient = models.CharField('机柜',max_length=128)
    name=models.CharField('服务器',max_length=32)
    node = models.ForeignKey('TreeNode', verbose_name='节点',
                            related_name='assets',
                            on_delete=models.CASCADE,null=True, blank=True)
    tag = models.ManyToManyField('Tag', verbose_name='标签',related_name='assets',null=True, blank=True)
    latest_date = models.DateField(verbose_name='更新时间', default=timezone.now, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    class Meta:
        verbose_name = "资产表"
        verbose_name_plural = verbose_name
        db_table = 'asset'
    def __str__(self):
        return self.name


class Server(models.Model):
    """服务器设备"""

    sub_asset_type_choice = (
        (0, 'PC服务器'),
        (1, '刀片机'),
        (2, '小型机'),
    )

    created_by_choice = (
        ('auto', '自动添加'),
        ('manual', '手工录入'),
    )
    asset = models.OneToOneField('Asset', on_delete=models.CASCADE,blank=True,default=0)  # 非常关键的一对一关联！asset被删除的时候一并删除server
    sub_asset_type = models.SmallIntegerField(choices=sub_asset_type_choice, default=0, verbose_name="服务器类型")
    host_name = models.CharField('主机名',max_length=255)
    manage_ip = models.GenericIPAddressField(verbose_name="IP地址",protocol="both",default='',blank=True,null=True)
    created_by = models.CharField(choices=created_by_choice, max_length=32, default='auto', verbose_name="添加方式")
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')
    raid_type = models.CharField(max_length=512, blank=True, null=True, verbose_name='Raid类型')
    os_type = models.CharField('操作系统类型', max_length=64, blank=True, null=True)
    os_distribution = models.CharField('发行商', max_length=64, blank=True, null=True)
    os_release = models.CharField('操作系统版本', max_length=64, blank=True, null=True)
    connection  = models.ForeignKey("Connection",verbose_name='连接表',
                            related_name='server',
                            on_delete=models.CASCADE,null=True, blank=True )

    def __str__(self):
        return self.model
    class Meta:
        verbose_name = '服务器'
        verbose_name_plural = verbose_name
        db_table = 'server'


class Connection(models.Model):
        user = models.CharField('ssh 用户',max_length=64)
        passwd = models.CharField('密码',max_length=1024)
        port = models.PositiveIntegerField('sshd 监听端口')
        # server = models.ManyToManyField('Server',verbose_name='服务器',related_name='conn')
        authed = models.BooleanField(verbose_name="是否认证",default=False,help_text="是否建立的认证关系")

        class Meta:
          verbose_name = '服务器连接表'
          verbose_name_plural = verbose_name
          db_table = 'connection'
        def __str__(self):
                return "服务器:{}-用户{}".format(self.server,self.user )
            
       
class InvertoryPool(models.Model):
     group = models.CharField("组名",max_length=64)
     serevr = models.ManyToManyField("Server",verbose_name="所属服务器",related_name="invertory")

     class Meta:
        verbose_name = "Ansible 资产清单"
        verbose_name_plural = verbose_name
        db_table="inventorypoll"

     def __str__(self):
      return "组.{}".format(self.group)

 
# class Variable(models.Model):

    #  """
    #  Ansible 变量表
    #  """
    #  key = models.CharField("变量名",max_length=64)
    #  val = models.CharField("变量值",max_length=512)
    #  host = models.ManyToManyField("Server",verbose_name="所属主机",related_name="var_server",blank=True,null=True)
    #  group = models.ManyToManyField("InvertoryPool",verbose_name="所属组",related_name="var_group",blank=True,null=True)

    #  class Meta:
    #     verbose_name = "Ansible 变量表"
    #     verbose_name_plural = verbose_name
    #     db_table="variable"

    #  def __str__(self):
    #   return "{}={}".format(self.key,self.val)


class Variable2Group(models.Model):
    """
    变量到组的关系表
    """
    key = models.CharField("变量名", max_length=64)
    val = models.CharField("变量值", max_length=512)
    group = models.ForeignKey("InvertoryPool",
                                 verbose_name="所属组",
                                 related_name="inv2vars",
                                 on_delete=models.CASCADE,
                                 blank=True, null=True)
    class Meta:
        verbose_name = "Ansible 组变量表"
        verbose_name_plural = verbose_name
        db_table = "variable_group"

    def __str__(self):
        return "{}:{}={}".format(self.group.group, self.key, self.val)

class Variable2Server(models.Model):
    """
    变量到主机的关系表
    """
    key = models.CharField("变量名", max_length=64, default='')
    val = models.CharField("变量值", max_length=512, default='')
    host = models.ForeignKey("Server",
                                 verbose_name="所属主机",
                                 related_name="server2vars",
                                 on_delete=models.CASCADE,
                                 blank=True, null=True)
    class Meta:
        verbose_name = "Ansible 主机变量表"
        verbose_name_plural = verbose_name
        db_table = "variable_host"

    def __str__(self):
        return "{}:{}={}".format(self.host.host_name, self.key, self.val)
