# Generated by Django 4.2.4 on 2023-08-31 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('_2_app', '0002_autor_alter_trow_trow_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autor',
            new_name='Author',
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('publication_date', models.DateField(auto_now=True)),
                ('category', models.CharField(max_length=100)),
                ('views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='_2_app.author')),
            ],
        ),
    ]
