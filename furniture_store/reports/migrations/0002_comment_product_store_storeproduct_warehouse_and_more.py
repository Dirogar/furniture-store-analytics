# Generated by Django 5.0.6 on 2024-07-12 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finish_planned_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('article', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Артикул')),
                ('name', models.CharField(max_length=254, verbose_name='Номенклатура')),
                ('model', models.CharField(max_length=254, null=True, verbose_name='Модель')),
                ('manufacturer', models.CharField(max_length=254, null=True, verbose_name='Производитель')),
                ('square', models.FloatField(null=True, verbose_name='Площадь номенклатуры')),
                ('category', models.CharField(max_length=254, null=True, verbose_name='Категория')),
                ('segment', models.CharField(max_length=254, null=True, verbose_name='Сегмент')),
                ('matrix', models.CharField(max_length=254, null=True, verbose_name='Матрица')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Название магазина')),
                ('area', models.FloatField(default=0, verbose_name='Площадь магазина')),
                ('users', models.ManyToManyField(blank=True, related_name='stores', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
        ),
        migrations.CreateModel(
            name='StoreProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('general_plan_exhibition', models.IntegerField(blank=True, null=True)),
                ('plan_exhibition', models.IntegerField(blank=True, null=True, verbose_name='План выставки')),
                ('fact_exhibition', models.IntegerField(blank=True, null=True, verbose_name='Факт выставки')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.store')),
            ],
            options={
                'verbose_name': 'Мебельный салон',
                'verbose_name_plural': 'Мебельные салоны',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.CreateModel(
            name='WarehouseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0, verbose_name='Остаток')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.warehouse')),
            ],
        ),
        migrations.DeleteModel(
            name='Shops',
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='comment',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.store'),
        ),
        migrations.AddField(
            model_name='store',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.warehouse'),
        ),
    ]
