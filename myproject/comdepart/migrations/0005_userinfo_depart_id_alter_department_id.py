# Generated by Django 5.1.4 on 2025-01-17 05:13

import django.db.models.fields.related
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comdepart', '0004_alter_department_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='depart_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.fields.related.ForeignKey, to='comdepart.department'),
        ),
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
