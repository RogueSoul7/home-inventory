# Generated by Django 3.1.6 on 2021-02-07 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210207_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='sate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.state'),
        ),
    ]
