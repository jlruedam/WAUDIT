# Generated by Django 3.2.3 on 2021-08-16 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Universo', '0004_auto_20210718_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditoriauniverso',
            name='riesgosAuditoria',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
