# Generated by Django 2.1.2 on 2018-10-24 04:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181024_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='raza',
            name='nombre',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
