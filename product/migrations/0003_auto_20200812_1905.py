# Generated by Django 3.1 on 2020-08-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200812_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FilePathField(path='D:\\roof_node\\cb_task\\product\\images'),
        ),
    ]