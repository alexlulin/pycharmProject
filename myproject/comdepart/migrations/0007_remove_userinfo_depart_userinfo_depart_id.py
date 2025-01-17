# Generated by Django 5.1.5 on 2025-01-17 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comdepart', '0006_rename_depart_id_userinfo_depart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='depart',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='depart_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comdepart.department', verbose_name='部门ID'),
        ),
    ]
