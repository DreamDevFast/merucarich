# Generated by Django 2.1.4 on 2020-05-06 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200326_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLSkipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', models.IntegerField(verbose_name='スキップ対象画面')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ')),
            ],
            options={
                'verbose_name': '一括相乗り検索URLスキップ要求',
                'verbose_name_plural': '一括相乗り検索URLスキップ要求',
            },
        ),
    ]
