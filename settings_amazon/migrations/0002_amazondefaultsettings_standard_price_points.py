# Generated by Django 2.1.4 on 2019-09-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_amazon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazondefaultsettings',
            name='standard_price_points',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='ポイント'),
        ),
    ]