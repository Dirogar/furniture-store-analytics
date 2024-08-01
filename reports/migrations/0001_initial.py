# Generated by Django 5.0.6 on 2024-07-30 12:27

import django.db.models.deletion
import reports.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='Код')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': ('Категория',),
                'verbose_name_plural': 'Категории',
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
            name='Product',
            fields=[
                ('article', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Артикул')),
                ('name', models.CharField(max_length=254, verbose_name='Номенклатура')),
                ('model', models.CharField(max_length=254, null=True, verbose_name='Модель')),
                ('manufacturer', models.CharField(max_length=254, null=True, verbose_name='Производитель')),
                ('square', models.FloatField(null=True, verbose_name='Площадь номенклатуры')),
                ('segment', models.CharField(max_length=254, null=True, verbose_name='Сегмент')),
                ('matrix', models.CharField(max_length=254, null=True, verbose_name='Матрица')),
                ('room_class', models.CharField(blank=True, max_length=8, null=True, verbose_name='Класс комнаты')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='category_product', to='reports.productcategory', verbose_name='Категория')),
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
                ('info', models.TextField(blank=True, null=True, verbose_name='Информация о салоне')),
                ('users', models.ManyToManyField(blank=True, related_name='stores', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('finish_planned_date', models.DateTimeField(validators=[reports.validators.validate_future_date], verbose_name='Планируемая дата выполнения')),
                ('status', models.CharField(default='Не выполнено', max_length=56, verbose_name='Статус комментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(db_column='product_article', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='reports.product', verbose_name='Товар')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='reports.store')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='StoreProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_exhibition', models.IntegerField(blank=True, null=True, verbose_name='План выставки')),
                ('fact_exhibition', models.IntegerField(blank=True, default=0, null=True, verbose_name='Факт выставки')),
                ('deviation', models.IntegerField(blank=True, default=0, null=True, verbose_name='Отклонение')),
                ('product', models.ForeignKey(db_column='product_article', on_delete=django.db.models.deletion.DO_NOTHING, related_name='store_products', to='reports.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='store_products', to='reports.store')),
            ],
            options={
                'verbose_name': 'Мебельный салон',
                'verbose_name_plural': 'Мебельные салоны',
            },
        ),
        migrations.CreateModel(
            name='WarehouseProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0, null=True, verbose_name='Остаток')),
                ('product', models.ForeignKey(db_column='product_article', on_delete=django.db.models.deletion.DO_NOTHING, related_name='warehouse_products', to='reports.product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='warehouse_products', to='reports.warehouse')),
            ],
            options={
                'verbose_name': 'Продукт на складе',
                'verbose_name_plural': 'Продукты на складе',
            },
        ),
        migrations.AddConstraint(
            model_name='storeproduct',
            constraint=models.UniqueConstraint(fields=('store', 'product'), name='unique_store_product'),
        ),
        migrations.AddConstraint(
            model_name='warehouseproduct',
            constraint=models.UniqueConstraint(fields=('warehouse', 'product'), name='unique_warehouse_product'),
        ),
    ]