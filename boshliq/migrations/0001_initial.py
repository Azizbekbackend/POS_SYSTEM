# Generated by Django 4.1 on 2022-08-31 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shtrix_code', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('mahsulot_turi', models.CharField(max_length=255)),
                ('mahsulot_hajmi', models.DecimalField(decimal_places=2, max_digits=9)),
                ('soni', models.PositiveIntegerField()),
                ('umumiy_miqdori', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kelgan_narxi', models.CharField(max_length=255)),
                ('foizi', models.CharField(max_length=255)),
                ('sotilish_narxi', models.CharField(max_length=255)),
                ('firmasi', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
