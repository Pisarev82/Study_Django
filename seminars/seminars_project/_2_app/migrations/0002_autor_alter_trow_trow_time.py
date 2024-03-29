# Generated by Django 4.2.4 on 2023-08-31 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('_2_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('biography', models.TextField()),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='trow',
            name='trow_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
