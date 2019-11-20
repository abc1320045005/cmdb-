from cmdb.models import InvertoryPool, Server

inv_dic = {"all": {"hosts": []}, "_meta": {"hostvars": {}}}

def add_var2group():
    '''为所有的组添加其变量, 并且添加组的主机'''
    # 获取到所有组的指定字段，queryset中的类型是[{},{}]
    invs = InventoryPool.objects.values(
        'group', 'inv2vars__key', 'inv2vars__val',
        'serevr__manage_ip'
    )


    for item in invs:
        # 假如组有组变量，就添加组变量和组成员
        if item['inv2vars__key']:
            inv_dic.setdefault(item['group'], {"vars": {}}
                              )["vars"].update({item['inv2vars__key']:item['inv2vars__val']})
            inv_dic[item['group']].setdefault('hosts', []).append(item['serevr__manage_ip'])

        else: # 没有组变量，仅添加组成员
            inv_dic.setdefault(item['group'],{"hosts": []}
                              )["hosts"].append(item['serevr__manage_ip'])

def add_host2all_hostvars():
    # 获取到所有主机的指定字段，queryset中的类型是[{},{}]
    qst_servers = Server.objects.values("host_name",
                                        "manager_ip",
                                        "server2vars__key",
                                        "server2vars__val")

    for server in qst_servers:
        # 添加所有的主机到 all组中
        inv_dic["all"]["hosts"].append(server["host_name"])

        # 假如主机有变量，添加变量到相应的主机中
        # 目标数据结构:
        # {'_meta': {'hostvars': {
        #  '172.16.153.130': {'key': 'gjzfap1','server_key': 'server'}
		# }}}
        if server["server2vars__key"]:
            key = server["server2vars__key"]
            val = server["server2vars__val"]
            inv_dic["_meta"]["hostvars"].setdefault(
                server["manage_ip"], {}).update({key:val})

def main():
    add_var2group()
    add_host2all_hostvars()
    return inv_dic

# 用法:
# 导入 此模块中的 main 函数
# 执行 main 函数 返回数据