# Generated by Django 4.0.2 on 2022-03-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orderupdate_remove_orders_update_desc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
        migrations.AddField(
            model_name='orders',
            name='update_desc',
            field=models.CharField(default='Placed', max_length=5000),
        ),
    ]
