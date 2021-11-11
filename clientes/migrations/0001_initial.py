# Generated by Django 3.2.9 on 2021-11-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]