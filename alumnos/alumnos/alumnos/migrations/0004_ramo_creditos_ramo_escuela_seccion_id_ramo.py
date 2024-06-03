# Generated by Django 5.0.6 on 2024-06-03 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_ramo_alter_seccion_id_seccion_seccionramo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ramo',
            name='creditos',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ramo',
            name='escuela',
            field=models.CharField(default=2, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seccion',
            name='id_ramo',
            field=models.ForeignKey(db_column='idRamo', default=1, on_delete=django.db.models.deletion.CASCADE, to='alumnos.ramo'),
            preserve_default=False,
        ),
    ]