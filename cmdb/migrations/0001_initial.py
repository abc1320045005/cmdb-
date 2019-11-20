# Generated by Django 2.1.5 on 2019-11-06 09:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type_id', models.CharField(choices=[('1', '服务器'), ('2', '路由器'), ('3', '交换机'), ('4', '防火墙')], default='1', max_length=1)),
                ('device_status_id', models.CharField(choices=[('1', '上架'), ('2', '在线'), ('3', '离线'), ('4', '下架')], default='1', max_length=1)),
                ('name', models.CharField(max_length=32, verbose_name='服务器')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '资产表',
                'verbose_name_plural': '资产表',
                'db_table': 'asset',
            },
        ),
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='机柜编号')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '机柜信息表',
                'verbose_name_plural': '机柜信息表',
                'db_table': 'cabinet',
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64, verbose_name='ssh 用户')),
                ('passwd', models.CharField(max_length=1024, verbose_name='密码')),
                ('port', models.PositiveIntegerField(verbose_name='sshd 监听端口')),
                ('authed', models.BooleanField(default=False, help_text='是否建立的认证关系', verbose_name='是否认证')),
            ],
            options={
                'verbose_name': '服务器连接表',
                'verbose_name_plural': '服务器连接表',
                'db_table': 'connection',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='机房名称')),
                ('addr', models.CharField(max_length=256, verbose_name='地址')),
                ('phone', models.CharField(max_length=11, verbose_name='联系电话')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '机房信息表',
                'verbose_name_plural': '机房信息表',
                'db_table': 'idc',
            },
        ),
        migrations.CreateModel(
            name='InvertoryPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=64, verbose_name='组名')),
            ],
            options={
                'verbose_name': 'Ansible 资产清单',
                'verbose_name_plural': 'Ansible 资产清单',
                'db_table': 'inventorypoll',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_asset_type', models.SmallIntegerField(choices=[(0, 'PC服务器'), (1, '刀片机'), (2, '小型机')], default=0, verbose_name='服务器类型')),
                ('host_name', models.CharField(max_length=255, verbose_name='主机名')),
                ('manage_ip', models.GenericIPAddressField(blank=True, default='', null=True, verbose_name='IP地址')),
                ('created_by', models.CharField(choices=[('auto', '自动添加'), ('manual', '手工录入')], default='auto', max_length=32, verbose_name='添加方式')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='服务器型号')),
                ('raid_type', models.CharField(blank=True, max_length=512, null=True, verbose_name='Raid类型')),
                ('os_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统类型')),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True, verbose_name='发行商')),
                ('os_release', models.CharField(blank=True, max_length=64, null=True, verbose_name='操作系统版本')),
                ('asset', models.OneToOneField(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='cmdb.Asset')),
                ('connection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server', to='cmdb.Connection', verbose_name='连接表')),
            ],
            options={
                'verbose_name': '服务器',
                'verbose_name_plural': '服务器',
                'db_table': 'server',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='标签')),
                ('latest_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新时间')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '标签信息表',
                'verbose_name_plural': '标签信息表',
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='TreeNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_name', models.CharField(max_length=128, verbose_name='节点名称')),
                ('node_upstream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_node', to='cmdb.TreeNode', verbose_name='上级节点')),
            ],
            options={
                'verbose_name': '服务树节点表',
                'verbose_name_plural': '服务树节点表',
                'db_table': 'tree_node',
            },
        ),
        migrations.CreateModel(
            name='Variable2Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='变量名')),
                ('val', models.CharField(max_length=512, verbose_name='变量值')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv2vars', to='cmdb.InvertoryPool', verbose_name='所属组')),
            ],
            options={
                'verbose_name': 'Ansible 组变量表',
                'verbose_name_plural': 'Ansible 组变量表',
                'db_table': 'variable_group',
            },
        ),
        migrations.CreateModel(
            name='Variable2Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=64, verbose_name='变量名')),
                ('val', models.CharField(default='', max_length=512, verbose_name='变量值')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='server2vars', to='cmdb.Server', verbose_name='所属主机')),
            ],
            options={
                'verbose_name': 'Ansible 主机变量表',
                'verbose_name_plural': 'Ansible 主机变量表',
                'db_table': 'variable_host',
            },
        ),
        migrations.AddField(
            model_name='invertorypool',
            name='serevr',
            field=models.ManyToManyField(related_name='invertory', to='cmdb.Server', verbose_name='所属服务器'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabinet', to='cmdb.IDC', verbose_name='所属机房'),
        ),
        migrations.AddField(
            model_name='asset',
            name='cabinet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asset', to='cmdb.Cabinet', verbose_name='所属机柜'),
        ),
        migrations.AddField(
            model_name='asset',
            name='node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='cmdb.TreeNode', verbose_name='节点'),
        ),
        migrations.AddField(
            model_name='asset',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='assets', to='cmdb.Tag', verbose_name='标签'),
        ),
    ]