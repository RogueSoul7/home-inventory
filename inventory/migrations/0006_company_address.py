# Generated by Django 3.1.6 on 2021-02-09 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20210207_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.address'),
        ),
    ]
