#!/usr/bin/env python
# -*- coding:utf-8 -*-
#import os,sys,subprocess
#import commands
#import re
raw_data=['eno16777736: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500',
          '        inet 172.16.8.44  netmask 255.255.255.0  broadcast 172.16.8.255',
          '        inet6 fe80::20c:29ff:fed7:5df9  prefixlen 64  scopeid 0x20<link>',
          '        ether 00:0c:29:d7:5d:f9  txqueuelen 1000  (Ethernet)',
          '        RX packets 21214  bytes 2178432 (2.0 MiB)',
          '        RX errors 0  dropped 0  overruns 0  frame 0',
          '        TX packets 5016  bytes 834010 (814.4 KiB)',
          '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0',
          '',
          'lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536',
          '        inet 127.0.0.1  netmask 255.0.0.0',
          '        inet6 ::1  prefixlen 128  scopeid 0x10<host>',
          '        loop  txqueuelen 0  (Local Loopback)',
          '        RX packets 137  bytes 15085 (14.7 KiB)',
          '        RX errors 0  dropped 0  overruns 0  frame 0',
          '        TX packets 137  bytes 15085 (14.7 KiB)',
          '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0',
          '',
          'virbr0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500',
          '        inet 192.168.122.1  netmask 255.255.255.0  broadcast 192.168.122.255',
          '        ether 00:00:00:00:00:00  txqueuelen 0  (Ethernet)',
          '        RX packets 0  bytes 0 (0.0 B)',
          '        RX errors 0  dropped 0  overruns 0  frame 0',
          '        TX packets 0  bytes 0 (0.0 B)',
          '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0',
          '',
          'virbr0-nic: flags=4098<BROADCAST,MULTICAST>  mtu 1500',
          '        ether 52:54:00:62:02:32  txqueuelen 500  (Ethernet)',
          '        RX packets 0  bytes 0 (0.0 B)',
          '        RX errors 0  dropped 0  overruns 0  frame 0',
          '        TX packets 0  bytes 0 (0.0 B)',
          '        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0',
          '']


def nicinfo():
    #tmp_f = file('/tmp/bonding_nic').read()
    #raw_data= subprocess.check_output("ifconfig -a",shell=True)
    #raw_data = commands.getoutput("ifconfig -a")

    #raw_data= raw_data.split("\n")

    nic_dic = {}
    dic ={}

    for line in raw_data:
        if line != "":
            if "eno" in line.split()[0]:
                #print "line:",line
                for last_mac_addr in raw_data:
                    #print (last_mac_addr)
                    if last_mac_addr != "":
                        if "eno" in last_mac_addr.split()[0]:
                            nic_name = last_mac_addr.split()[0]
                            dic['name'] = nic_name
                        else:
                            nic_name=None

                        mac_addr1 = last_mac_addr.split("ether")
                        #print ('mac_addr1:',mac_addr1)
                        if len(mac_addr1)>1:
                            mac_addr = mac_addr1[1].split()[0]
                            #print (mac_addr)
                            dic['macaddress']=mac_addr
                        else:
                            mac_addr = None

                        raw_ip_addr = last_mac_addr.split("inet")
                        raw_bcast = last_mac_addr.split("broadcast")
                        #print (raw_bcast)
                        raw_netmask = last_mac_addr.split("netmask")
                        if len(raw_bcast) > 1:  # has addr
                            ip_addr = raw_ip_addr[1].split()[0]
                            network = raw_bcast[1].split()[0]
                            netmask = raw_netmask[1].split()[0]
                            dic['ipaddress'] = ip_addr
                            dic['network'] = network
                            dic['netmask'] = netmask
                            dic['bonding'] = 1
                            dic['model'] = 'unknown'
                        else:
                            ip_addr = None
                            network = None
                            netmask = None

                        if 'macaddress' in dic:
                            nic_dic[mac_addr] = dic
                            #print (nic_dic)
                            dic={}
                            break
    nic_list = []
    for k, v in nic_dic.items():
        nic_list.append(v)
        print (nic_list)
        return {'nic': nic_list}

nicinfo()





