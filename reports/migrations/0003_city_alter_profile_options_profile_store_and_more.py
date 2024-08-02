# Generated by Django 5.0.6 on 2024-08-01 11:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Допольнительная информация'},
        ),
        migrations.AddField(
            model_name='profile',
            name='store',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='reports.store', verbose_name='Мебельный салон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_position',
            field=models.TextField(blank=True, max_length=100, verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='reports.city', verbose_name='Город'),
            preserve_default=False,
        ),
    ]