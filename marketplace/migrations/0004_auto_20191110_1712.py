# Generated by Django 2.2.5 on 2019-11-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20191104_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_photo',
            field=models.ImageField(default='static/marketplace/default.png', upload_to='media/'),
        ),
    ]
