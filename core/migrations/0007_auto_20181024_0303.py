# Generated by Django 2.1.2 on 2018-10-24 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181024_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='EstadoMascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.EstadoMascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='GeneroMascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.GeneroMascota'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='Raza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Raza'),
        ),
    ]
