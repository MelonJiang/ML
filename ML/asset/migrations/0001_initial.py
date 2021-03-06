# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-01 11:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u4e1a\u52a1\u540d\u79f0')),
                ('memo', models.TextField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u540d\u79f0',
                'verbose_name_plural': '\u4e1a\u52a1\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(choices=[('server', '\u670d\u52a1\u5668'), ('switch', '\u4ea4\u6362\u673a'), ('router', '\u8def\u7531\u5668'), ('firewall', '\u9632\u706b\u5899'), ('storage', '\u5b58\u50a8\u8bbe\u5907'), ('NLB', 'NetScaler'), ('wireless', '\u65e0\u7ebfAP'), ('software', '\u8f6f\u4ef6\u8d44\u4ea7'), ('others', '\u5176\u4ed6\u7c7b')], default='server', max_length=64)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u5e8f\u5217\u53f7')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='\u8d44\u4ea7SN\u53f7')),
                ('management_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u7ba1\u7406IP')),
                ('idc_jg', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u673a\u67dc\u7f16\u53f7')),
                ('status', models.IntegerField(blank=True, choices=[(1, '\u5728\u7528'), (2, '\u505c\u7528')], default=1, null=True, verbose_name='\u4f7f\u7528\u72b6\u6001')),
                ('trade_date', models.DateField(blank=True, null=True, verbose_name='\u8d2d\u4e70\u65f6\u95f4')),
                ('expire_date', models.DateField(blank=True, null=True, verbose_name='\u8fc7\u4fdd\u4fee\u671f')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='\u4ef7\u683c')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
                'verbose_name_plural': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u4e1a\u52a1\u7ebf\u540d\u79f0')),
                ('memo', models.TextField(blank=True, max_length=64, null=True, verbose_name='\u5907\u6ce8')),
                ('parent_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_level', to='asset.BusinessUnit')),
            ],
            options={
                'verbose_name': '\u4e1a\u52a1\u7ebf',
                'verbose_name_plural': '\u4e1a\u52a1\u7ebf',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=128, unique=True, verbose_name='\u5408\u540c\u53f7')),
                ('name', models.CharField(max_length=64, verbose_name=' \u5408\u540c\u540d\u79f0')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('price', models.IntegerField(verbose_name='\u5408\u540c\u91d1\u989d')),
                ('detile', models.TextField(blank=True, null=True, verbose_name='\u5408\u540c\u660e\u7ec6')),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('license_num', models.IntegerField(blank=True, verbose_name='license\u6570\u91cf')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u5408\u540c',
                'verbose_name_plural': '\u5408\u540c',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_model', models.CharField(blank=True, max_length=128, verbose_name='CPU\u578b\u53f7')),
                ('cpu_count', models.SmallIntegerField(verbose_name='\u7269\u7406cpu\u4e2a\u6570')),
                ('cpu_core_count', models.SmallIntegerField(verbose_name='cpu\u6838\u6570')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': 'CPU\u90e8\u4ef6',
                'verbose_name_plural': 'CPU\u90e8\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u53f7')),
                ('slot', models.CharField(max_length=64, verbose_name='\u63d2\u69fd\u4f4d')),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5236\u9020\u5546')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u78c1\u76d8\u578b\u53f7')),
                ('capacity', models.FloatField(verbose_name='\u78c1\u76d8\u5bb9\u91cfGB')),
                ('iface_type', models.CharField(choices=[('SATA', 'SATA'), ('SAS', 'SAS'), ('SCSI', 'SCSI'), ('SSD', 'SSD')], default='SAS', max_length=64, verbose_name='\u63a5\u53e3\u7c7b\u578b')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': '\u786c\u76d8',
                'verbose_name_plural': '\u786c\u76d8',
            },
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u4e8b\u4ef6\u540d\u79f0')),
                ('event_type', models.SmallIntegerField(choices=[(1, '\u786c\u4ef6\u53d8\u66f4'), (2, '\u65b0\u589e\u914d\u4ef6'), (3, '\u8bbe\u5907\u4e0b\u7ebf'), (4, '\u8bbe\u5907\u4e0a\u7ebf'), (5, '\u5b9a\u671f\u7ef4\u62a4'), (6, '\u4e1a\u52a1\u4e0a\u7ebf\\\u66f4\u65b0\\\u53d8\u66f4'), (7, '\u5176\u5b83'), (7, 'IDC\u4fe1\u606f')], verbose_name='\u4e8b\u4ef6\u7c7b\u578b')),
                ('component', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4e8b\u4ef6\u5b50\u9879')),
                ('detail', models.TextField(verbose_name='\u4e8b\u4ef6\u8be6\u60c5')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u4e8b\u4ef6\u65f6\u95f4')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': '\u4e8b\u4ef6\u7eaa\u5f55',
                'verbose_name_plural': '\u4e8b\u4ef6\u7eaa\u5f55',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('idc_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u673a\u623f\u7c7b\u578b')),
                ('idc_location', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u673a\u623f\u4f4d\u7f6e')),
                ('idc_contacts', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('memo', models.TextField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u673a\u623f',
                'verbose_name_plural': '\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Linkman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u59d3\u540d')),
                ('phone', models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u53f7\u7801')),
                ('department', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u90e8\u95e8')),
                ('email', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u90ae\u7bb1')),
                ('qq', models.CharField(blank=True, max_length=64, null=True, verbose_name='QQ')),
            ],
            options={
                'verbose_name': '\u8054\u7cfb\u4eba\u5217\u8868',
                'verbose_name_plural': '\u8054\u7cfb\u4eba\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufactory', models.CharField(max_length=64, unique=True, verbose_name='\u5382\u5546\u540d\u79f0')),
                ('support_num', models.CharField(blank=True, max_length=32, verbose_name='\u652f\u6301\u7535\u8bdd')),
                ('memo', models.TextField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u5382\u5546',
                'verbose_name_plural': '\u5382\u5546',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlan_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u5185\u7f51IP')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u53f7')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u578b\u53f7')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='\u7aef\u53e3\u4e2a\u6570')),
                ('device_detail', models.TextField(blank=True, null=True, verbose_name='\u8bbe\u7f6e\u8be6\u7ec6\u914d\u7f6e')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': '\u7f51\u7edc\u8bbe\u5907',
                'verbose_name_plural': '\u7f51\u7edc\u8bbe\u5907',
            },
        ),
        migrations.CreateModel(
            name='NewAssetApprovalZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='\u8d44\u4ea7SN\u53f7')),
                ('asset_type', models.CharField(blank=True, choices=[('server', '\u670d\u52a1\u5668'), ('switch', '\u4ea4\u6362\u673a'), ('router', '\u8def\u7531\u5668'), ('firewall', '\u9632\u706b\u5899'), ('storage', '\u5b58\u50a8\u8bbe\u5907'), ('NLB', 'NetScaler'), ('wireless', '\u65e0\u7ebfAP'), ('software', '\u8f6f\u4ef6\u8d44\u4ea7'), ('others', '\u5176\u5b83\u7c7b')], max_length=64, null=True)),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True)),
                ('model', models.CharField(blank=True, max_length=128, null=True)),
                ('ram_size', models.IntegerField(blank=True, null=True)),
                ('cpu_model', models.CharField(blank=True, max_length=128, null=True)),
                ('cpu_count', models.IntegerField(blank=True, null=True)),
                ('cpu_core_count', models.IntegerField(blank=True, null=True)),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True)),
                ('os_type', models.CharField(blank=True, max_length=64, null=True)),
                ('os_release', models.CharField(blank=True, max_length=64, null=True)),
                ('data', models.TextField(verbose_name='\u8d44\u4ea7\u6570\u636e')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u6c47\u62a5\u65e5\u671f')),
                ('approved', models.BooleanField(default=False, verbose_name='\u5df2\u6279\u51c6')),
                ('approved_date', models.DateTimeField(blank=True, null=True, verbose_name='\u6279\u51c6\u65e5\u671f')),
            ],
            options={
                'verbose_name': '\u65b0\u4e0a\u7ebf\u5f85\u6279\u51c6\u8d44\u4ea7',
                'verbose_name_plural': '\u65b0\u4e0a\u7ebf\u5f85\u6279\u51c6\u8d44\u4ea7',
            },
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u7f51\u5361\u540d')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u53f7')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u7f51\u5361\u578b\u53f7')),
                ('macaddress', models.CharField(max_length=64, unique=True, verbose_name='MAC')),
                ('ipaddress', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP')),
                ('netmask', models.CharField(blank=True, max_length=64, null=True)),
                ('bonding', models.CharField(blank=True, max_length=64, null=True)),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': '\u7f51\u5361',
                'verbose_name_plural': '\u7f51\u5361',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u6743\u9650\u540d\u79f0')),
                ('url', models.CharField(max_length=255, verbose_name='URL\u540d\u79f0')),
                ('per_method', models.SmallIntegerField(choices=[(1, 'GET'), (2, 'POST')], default=1, verbose_name='\u8bf7\u6c42\u65b9\u6cd5')),
                ('argument_list', models.CharField(blank=True, help_text='\u591a\u4e2a\u53c2\u6570\u4e4b\u95f4\u7528\u82f1\u6587\u534a\u89d2\u9017\u53f7\u9694\u5f00', max_length=255, null=True, verbose_name='\u53c2\u6570\u5217\u8868')),
                ('describe', models.CharField(max_length=255, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u6743\u9650\u8868',
                'verbose_name_plural': '\u6743\u9650\u8868',
                'permissions': (('view_asset_create', '\u521b\u5efa\u8d44\u4ea7'), ('view_asset_compile', '\u7f16\u8f91\u8d44\u4ea7'), ('view_asset_delete', '\u5220\u9664\u8d44\u4ea7'), ('btn_asset_create', '\u521b\u5efa\u6309\u94ae'), ('btn_asset_compile', '\u7f16\u8f91\u6309\u94ae'), ('btn_asset_delete', '\u5220\u9664\u6309\u94ae')),
            },
        ),
        migrations.CreateModel(
            name='Projectname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u9879\u76ee\u540d\u79f0')),
                ('memo', models.TextField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u540d\u79f0',
                'verbose_name_plural': '\u9879\u76ee\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='RaidAdaptor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u53f7')),
                ('slot', models.CharField(max_length=64, verbose_name='\u63d2\u53e3')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u578b\u53f7')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u53f7')),
                ('model', models.CharField(max_length=128, verbose_name='\u5185\u5b58\u578b\u53f7')),
                ('slot', models.CharField(max_length=64, verbose_name='\u63d2\u69fd')),
                ('manufactory', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u5236\u9020\u5546')),
                ('capacity', models.IntegerField(verbose_name='\u5185\u5b58\u5927\u5c0f(MB)')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
            ],
            options={
                'verbose_name': 'RAM',
                'verbose_name_plural': 'RAM',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(choices=[('auto', 'Auto'), ('manual', 'Manual')], default='auto', max_length=32)),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u578b\u53f7')),
                ('raid_type', models.CharField(blank=True, max_length=512, null=True, verbose_name='raid\u7c7b\u578b')),
                ('os_type', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7c7b\u578b')),
                ('os_distribution', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u53d1\u578b\u7248\u672c')),
                ('os_release', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf\u7248\u672c')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset')),
                ('hosted_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_on_server', to='asset.Server')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668',
                'verbose_name_plural': '\u670d\u52a1\u5668',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('linux', 'Linux'), ('windows', 'Windows'), ('network_firmware', 'Network Firmware'), ('software', 'Softwares')], default=1, help_text='eg. GNU/Linux', max_length=64, verbose_name='\u7cfb\u7edf\u7c7b\u578b')),
                ('distribution', models.CharField(choices=[('windows', 'Windows'), ('centos', 'CentOS'), ('ubuntu', 'Ubuntu')], default='windows', max_length=32, verbose_name='\u53d1\u578b\u7248\u672c')),
                ('version', models.CharField(help_text='eg. CentOS release 6.5 (Final)', max_length=64, unique=True, verbose_name='\u8f6f\u4ef6/\u7cfb\u7edf\u7248\u672c')),
                ('language', models.CharField(choices=[('cn', '\u4e2d\u6587'), ('en', '\u82f1\u6587')], default='cn', max_length=32, verbose_name='\u7cfb\u7edf\u8bed\u8a00')),
            ],
            options={
                'verbose_name': '\u8f6f\u4ef6/\u7cfb\u7edf',
                'verbose_name_plural': '\u8f6f\u4ef6/\u7cfb\u7edf',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u59d3\u540d')),
                ('token', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='token')),
                ('department', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u90e8\u95e8')),
                ('tel', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u5ea7\u673a')),
                ('mobile', models.CharField(blank=True, default=None, max_length=32, null=True, verbose_name='\u624b\u673a')),
                ('memo', models.TextField(blank=True, default=None, null=True, verbose_name='\u5907\u6ce8')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u5217\u8868',
                'verbose_name_plural': '\u7528\u6237\u5217\u8868',
            },
        ),
        migrations.AddField(
            model_name='newassetapprovalzone',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.UserProfile', verbose_name='\u6279\u51c6\u4eba'),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='firmware',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Software'),
        ),
        migrations.AddField(
            model_name='eventlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.UserProfile', verbose_name='\u4e8b\u4ef6\u6e90'),
        ),
        migrations.AddField(
            model_name='asset',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.UserProfile', verbose_name='\u8d44\u4ea7\u7ba1\u7406\u5458'),
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.BusinessUnit', verbose_name='\u6240\u5c5e\u4e1a\u52a1\u7ebf'),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.IDC', verbose_name='IDC\u673a\u623f'),
        ),
        migrations.AddField(
            model_name='asset',
            name='linkman',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Linkman', verbose_name='\u8054\u7cfb\u4eba'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufactory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.Manufactory', verbose_name='\u5236\u9020\u5546'),
        ),
        migrations.AddField(
            model_name='application',
            name='asset',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset'),
        ),
        migrations.AlterUniqueTogether(
            name='ram',
            unique_together=set([('asset', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='raidadaptor',
            unique_together=set([('asset', 'slot')]),
        ),
        migrations.AlterUniqueTogether(
            name='disk',
            unique_together=set([('asset', 'slot')]),
        ),
    ]
