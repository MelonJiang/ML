#!/usr/bin/env python
# -*- coding:utf-8 -*-
import platform
import win32com
import wmi

def collect():
    data={
        'os_type':platform.system(),
        'os_release':'%s %s %s'%(platform.release(),platform.architecture()[0],platform.version()),
        'os_distribution': 'Microsoft',
        'asset_type':'server'
    }

    obj = win_collect()
    data.update(obj.get_cpu())
    data.update(obj.get_ram())
    data.update(obj.get_server())
    data.update(obj.get_disk())
    data.update(obj.get_nic())

    #for k,v in data.items():
    #    print k,v
    return data

class win_collect(object):
    def __init__(self):
        self.wmi_obj = wmi.WMI()
        self.wmi_service_obj = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        self.wmi_service_connector =self.wmi_service_obj.ConnectServer(".","root\cimv2")

    def get_cpu(self):
        data = {}
        cpu_lists = self.wmi_obj.Win32_Processor()
        cpu_core_count = 0

        for cpu in cpu_lists:
            cpu_core_count += cpu.NumberOfCores
            cpu_model = cpu.Name
        data["cpu_count"] = len(cpu_lists)
        data["cpu_model"] = cpu_model
        data["cpu_core_count"] =cpu_core_count
        return data

    def get_ram(self):
        data = []
        ram_collections = self.wmi_service_connector.ExecQuery("Select * from Win32_PhysicalMemory")
        for item in ram_collections:
            item_data = {}
            #print item
            mb = int(1024 * 1024)
            ram_size = int(item.Capacity) / mb
            item_data = {
                "slot":item.DeviceLocator.strip(),
                "capacity":ram_size,
                "model":item.Caption,
                "manufactory":item.Manufacturer,
                "sn":item.SerialNumber,
            }
            data.append(item_data)
        #for i in data:
        #    print i
        return {"ram":data}
    def get_server(self):
        computer_info =  self.wmi_obj.Win32_ComputerSystem()[0]
        system_info =  self.wmi_obj.Win32_OperatingSystem()[0]
        data = {}
        data['manufactory'] = computer_info.Manufacturer
        data['model'] = computer_info.Model
        data['wake_up_type'] = computer_info.WakeUpType
        data['sn'] = system_info.SerialNumber
        #print data
        return data

    def get_disk(self):
        data = []
        for disk in self.wmi_obj.Win32_DiskDrive():
            #print  disk.Model,disk.Size,disk.DeviceID,disk.Name,disk.Index,disk.SerialNumber,disk.SystemName,disk.Description
            item_data = {}
            iface_choices = ["SAS","SCSI","SATA","SSD"]
            for iface in iface_choices:
                if iface in disk.Model:
                    item_data['iface_type']  = iface
                    break
            else:
                item_data['iface_type']  = 'unknown'
            item_data['slot']  = disk.Index
            item_data['sn']  = disk.SerialNumber
            item_data['model']  = disk.Model
            item_data['manufactory']  = disk.Manufacturer
            item_data['capacity']  = int(disk.Size ) / (1024*1024*1024)
            data.append(item_data)
        return {'physical_disk_driver':data}
    def get_nic(self):
        data = []
        for nic in self.wmi_obj.Win32_NetworkAdapterConfiguration():
            if nic.MACAddress is not None:
                item_data = {}
                item_data['macaddress'] = nic.MACAddress
                item_data['model'] = nic.Caption
                item_data['name'] = nic.Index
                if nic.IPAddress  is not None:
                    item_data['ipaddress'] = nic.IPAddress[0]
                    item_data['netmask'] = nic.IPSubnet
                else:
                    item_data['ipaddress'] = ''
                    item_data['netmask'] = ''
                bonding = 0
                #print nic.MACAddress ,nic.IPAddress,nic.ServiceName,nic.Caption,nic.IPSubnet
                #print item_data
                data.append(item_data)
        return {'nic':data}

if __name__=="__main__":
    collect()
