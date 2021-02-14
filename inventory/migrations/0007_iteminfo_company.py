# Generated by Django 3.1.6 on 2021-02-09 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_company_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='iteminfo',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.company'),
        ),
    ]