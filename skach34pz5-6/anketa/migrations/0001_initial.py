# Generated by Django 4.2.1 on 2023-10-20 12:57

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grazhdanin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(upload_to='', verbose_name='Аватар')),
                ('nomer', models.TextField(max_length=50, verbose_name='Номер Телефона')),
                ('sertific', models.FileField(max_length=255, upload_to='', verbose_name='Сертификат')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-id'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Naviki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Навыки')),
            ],
            options={
                'verbose_name': 'Навыки',
                'verbose_name_plural': 'Навыки',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Proffessia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Sertifikat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Тип')),
                ('polniy', models.FileField(max_length=255, upload_to='', verbose_name='Сертификат')),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Voprosi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='Вопросы')),
                ('ball', models.IntegerField(verbose_name='Баллы')),
                ('navik', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anketa.naviki', verbose_name='Навык')),
            ],
            options={
                'verbose_name': 'Вопросы',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='ModelProf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ball', models.IntegerField(verbose_name='Баллы')),
                ('navik', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='anketa.naviki', verbose_name='Навык')),
                ('prof', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Модельная профессия',
                'verbose_name_plural': 'Модельные профессии',
                'ordering': ['-navik'],
            },
        ),
    ]
