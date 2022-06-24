# Generated by Django 3.1.7 on 2022-06-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TablaEmpleado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('profesion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TablaNomina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profesion', models.CharField(max_length=100)),
                ('salario', models.CharField(max_length=100)),
                ('jornada', models.CharField(max_length=100)),
            ],
        ),
    ]