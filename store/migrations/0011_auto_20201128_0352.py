# Generated by Django 3.1.2 on 2020-11-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20201128_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description1',
            field=models.CharField(default='', max_length=2550, null=True),
        ),
    ]
