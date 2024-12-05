# Generated by Django 5.1.4 on 2024-12-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
