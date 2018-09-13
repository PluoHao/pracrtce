# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-13 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aname', models.CharField(max_length=50, verbose_name='收货人')),
                ('Aphone', models.CharField(max_length=11, verbose_name='手机')),
                ('ADS', models.CharField(max_length=200, verbose_name='地址')),
                ('orderId', models.CharField(max_length=30, verbose_name='订单号')),
            ],
            options={
                'verbose_name_plural': '地址',
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50, verbose_name='用户名')),
                ('upassword', models.CharField(max_length=200, verbose_name='密码')),
                ('uphone', models.CharField(max_length=11, verbose_name='手机号')),
                ('identity', models.CharField(max_length=18, verbose_name='身份证')),
                ('isactive', models.BooleanField(default=True, verbose_name='状态')),
            ],
            options={
                'verbose_name_plural': '用户',
                'db_table': 'USER',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='USER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercise.USER'),
        ),
    ]
