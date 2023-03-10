# Generated by Django 2.1.4 on 2019-11-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_itemcandidatetocsv'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverrideConstantValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=256, verbose_name='システム変数名')),
                ('value', models.CharField(max_length=256, verbose_name='アイテム変数の値')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='開始日時')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name': 'システム変数変更',
                'verbose_name_plural': 'システム変数変更',
            },
        ),
    ]
