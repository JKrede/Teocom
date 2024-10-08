# Generated by Django 5.1.1 on 2024-09-26 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('ubicacion', models.CharField(max_length=30)),
                ('temperatura', models.IntegerField()),
                ('humedad', models.DecimalField(decimal_places=2, max_digits=2)),
                ('presion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=30, unique=True)),
                ('clave', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('administrador', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ValorCriticoHumedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=30)),
                ('humedad_maxima', models.IntegerField()),
                ('humedad_minima', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ValorCriticoPresion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=30)),
                ('presion_maxima', models.IntegerField()),
                ('presion_minima', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ValorCriticoTemperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=30)),
                ('temperatura_maxima', models.IntegerField()),
                ('temperatura_minima', models.IntegerField()),
            ],
        ),
    ]
