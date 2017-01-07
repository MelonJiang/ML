# -*-coding:utf-8 -*-
from asset import models
import json

def get_asset_model(obj):
    asset_tables = ['server','networkdevice','software']
    for asset_type in asset_tables:
        if hasattr(obj,asset_type):
            ass_obj =getattr(obj,asset_type)
            return ass_obj.model

def fetch_new_asset_list():
    asset_list = models.NewAssetApprovalZone.objects.all()
    data_list = []
    for obj in asset_list:
        data = {
            'id':obj.id,
            'choice':"",
            'sn': obj.sn,
            'asset_type': obj.asset_type,
            'manufactory': obj.manufactory,
            'model': obj.model,
            'cpu_model' :obj.cpu_model,
            'cpu_core_count' :obj.cpu_core_count,
            'cpu_count' : obj.cpu_count,
            'ram_size': obj.ram_size,
            'date':(obj.date).strftime("%Y-%m-%d %H:%M:%S")
        }
        print(data)
        data_list.append(data)
    return  {'data':data_list}


def fetch_asset_list():
    '''获取显示的资产列表'''
    asset_list = models.Asset.objects.all()
    data_list = []
    for obj in asset_list:
        data={
            'asset_id' : obj.id,
            'sn': obj.sn,
            'serial_name':obj.name,
            'asset_type' : obj.get_asset_type_display(),
            'ip' : obj.management_ip,
           # 'hostname' : obj.hostname,
            'projectname' : None if not obj.projectname else obj.projectname.name,
            'application' : None if not obj.application else obj.application.name,
            'module' : obj.module,
            'idc_name' : None if not obj.idc else obj.idc.name,
            'idc_jg' : obj.idc_jg,
            'status' : obj.get_status_display(),
            'linkman' : None if not obj.linkman else obj.linkman.name,
            'admin' : None if not obj.admin else obj.admin.name,
            'memo' : obj.memo,
            'details': '详细',
        }
        data_list.append(data)
    return {'data': data_list}


def fetch_asset_linkman():
    '''获取联系人列表'''
    linkman_list = models.Linkman.objects.all()
    data_linkman = []
    for obj in linkman_list:
        data={
            'id' : obj.id,
            'choice': '',
            'department':obj.department,
            'name' : obj.name,
            'fixed_phone' : obj.fixed_phone,
            'phone' : obj.phone,
            'email' : obj.email,
            'qq' : obj.qq,
            'memo' : obj.memo,
        }
        data_linkman.append(data)
    return {'data': data_linkman}


def fetch_asset_event_logs():
    '''获取审计列表'''
    log_list = models.EventLog.objects.order_by('-id').all()    #倒序
    print ("log_list",log_list)
    data_list = []

    for log in log_list:
        print log.user
        data = {
            'id':log.id,
            'event_type':log.get_event_type_display(),
            'name':log.name,
            'component':log.component,
            'detail':log.detail,
            'user':log.user.username,
            'date':(log.date).strftime("%Y-%m-%d %H:%M:%S"),
        }
        data_list.append(data)
    print(data_list)
    return {"data":data_list}


class LogicalProcess(object):

    def __init__(self,request_obj):
        self.request = request_obj

    # 编辑
    def modification(self,user_id):
        '''编辑'''
        serial_name = self.request.get('serial_name')
        asset_obj = models.Asset.objects.get(name=serial_name)
        data_dic = {
            'asset_type': [asset_obj.asset_type, self.request.get('asset_type')],
            'management_ip' : [asset_obj.management_ip, self.request.get('ip')],
            'name': [asset_obj.name, self.request.get('serial_name')],
            'module' : [asset_obj.module, self.request.get('module')],
            'status' : [asset_obj.status, int(self.request.get('status'))],
            'memo' : [asset_obj.memo, self.request.get('memo')],
            'idc_jg' : [asset_obj.idc_jg, self.request.get('idc_jg')],
        }
        # log_dic = {}
        for k,v in data_dic.items():
            if v[0] != v[1]:
                db_field_obj = asset_obj._meta.get_field(k)  #取出该字段的对象
                db_field_obj.save_form_data(asset_obj, v[1])    #把字段内容改为字典传入的内容
                asset_obj.save() #保存

        idc = int(self.request.get('idc_type'))
        linkman = int(self.request.get('linkman_type'))
        projectname  = int(self.request.get('projectname'))
        application = int(self.request.get('application'))

        if idc != asset_obj.idc_id:
            asset_obj.idc_id = idc
            asset_obj.save()
        if linkman != asset_obj.linkman_id:
            asset_obj.linkman_id = linkman
            asset_obj.save()
        if projectname != asset_obj.application_id:
            asset_obj.projectname_id = projectname
            asset_obj.save()
        if application != asset_obj.application_id:
            asset_obj.application_id = application
            asset_obj.save()


        log_msg = u"编辑信息成功"
        self.log_handler(2,user_id,7,log_msg, serial_name)

    # 创建
    def asset_create(self,user_id):
        '''新建'''
        print self.request
        serial_name = self.request.get('serial_name')
        data_dic = {
            'asset_type':self.request.get('asset_type'),
            'management_ip': self.request.get('ip'),
            'name': self.request.get('serial_name'),
            'projectname_id': int(self.request.get('projectname')),
            'application_id': int(self.request.get('application')),
            'module': self.request.get('module'),
            'idc_id': int(self.request.get('idc_type')),
            'status': int(self.request.get('status')),
            'linkman_id': int(self.request.get('linkman_type')),
            'memo': self.request.get('memo'),
            'idc_jg': self.request.get('idc_jg'),
        }
        obj = models.Asset(**data_dic)
        obj.save()
        log_msg = u'创建IDC信息成功'
        print log_msg
        self.log_handler(1,user_id,7,log_msg,serial_name)


    # 删除
    def asset_delete(self,user_id):
        '''删除'''
        li_obj = self.request.get('obj')
        li = json.loads(li_obj)

        for i in li:
            i = int(i)
            hostlist_obj = models.Asset.objects.get(id=i)

            log_msg = u'删除IDC信息成功'
            self.log_handler(3, user_id, 7, log_msg, hostlist_obj.name)
            hostlist_obj.delete()   #删除


    # 记录日志
    def log_handler(self,handle_type,user_id,event_type,log_msg,component=None):
        log_event={
            1 : u'新增',
            2 : u'编辑',
            3 : u'删除',
        }

        log_obj = models.EventLog(
            name = log_event[handle_type],
            event_type = event_type,
            component = component,
            detail = log_msg,
            user_id = user_id
        )
        log_obj.save()



