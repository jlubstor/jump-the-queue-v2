# Generated by Django 2.2.4 on 2019-08-08 07:41

import accesscodemanagement.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('queuemanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modificationCounter', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=4)),
                ('uuid', models.CharField(max_length=36)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('startTime', models.DateTimeField(blank=True, null=True)),
                ('endTime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[(accesscodemanagement.models.AccessCodeStatus('WAITING'), 'WAITING'), (accesscodemanagement.models.AccessCodeStatus('ATTENDING'), 'ATTENDING'), (accesscodemanagement.models.AccessCodeStatus('ATTENDED'), 'ATTENDED'), (accesscodemanagement.models.AccessCodeStatus('SKIPPED'), 'SKIPPED'), (accesscodemanagement.models.AccessCodeStatus('NOTSTARTED'), 'NOTSTARTED')], max_length=10)),
                ('queueId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queuemanagement.Queue')),
            ],
            options={
                'ordering': ('createdDate',),
            },
        ),
    ]