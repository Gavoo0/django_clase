# Generated by Django 4.1.2 on 2024-06-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id_seccion', models.AutoField(db_column='id_seccion', primary_key=True, serialize=False)),
                ('seccion', models.CharField(max_length=100)),
            ],
        ),
    ]
