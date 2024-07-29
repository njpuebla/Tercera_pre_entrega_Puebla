# Generated by Django 5.0.7 on 2024-07-28 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amplificadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=70)),
                ('modelo', models.CharField(max_length=70)),
                ('watts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Efectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=70)),
                ('modelo', models.CharField(max_length=70)),
                ('trueByPass', models.BooleanField()),
                ('buffer', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Guitarras_acusticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=70)),
                ('modelo', models.CharField(max_length=70)),
                ('cantidadDeCuerdas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guitarras_electricas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=70)),
                ('modelo', models.CharField(max_length=70)),
                ('cantidadDeCuerdas', models.IntegerField()),
            ],
        ),
    ]
