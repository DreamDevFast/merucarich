# Generated by Django 2.1.4 on 2020-02-12 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercari', '0002_mercaritoamazonitemcandidate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mercariexcludeseller',
            options={'verbose_name': '禁止セラー個別設定', 'verbose_name_plural': '禁止セラー個別設定'},
        ),
        migrations.AlterModelOptions(
            name='mercariexcludesellermaster',
            options={'verbose_name': '新規ユーザー禁止セラーマスタ', 'verbose_name_plural': '新規ユーザー禁止セラーマスタ'},
        ),
    ]
