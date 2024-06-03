# Generated by Django 4.1.2 on 2024-06-02 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_seccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id_ramo', models.AutoField(db_column='idRamo', primary_key=True, serialize=False)),
                ('ramo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='seccion',
            name='id_seccion',
            field=models.AutoField(db_column='idSeccion', primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='SeccionRamo',
            fields=[
                ('id_SeccionRamo', models.AutoField(db_column='idSeccionRamo', primary_key=True, serialize=False)),
                ('id_alumno', models.ForeignKey(db_column='idAlumno', on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno')),
                ('id_seccion', models.ForeignKey(db_column='Seccion', on_delete=django.db.models.deletion.CASCADE, to='alumnos.seccion')),
            ],
        ),
    ]