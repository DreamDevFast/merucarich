# Generated by Django 2.1.4 on 2019-05-06 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190108_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannedKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banned_keyword', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '禁止ワード',
                'verbose_name_plural': '禁止ワード',
            },
        ),
    ]
