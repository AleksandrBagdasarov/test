# Generated by Django 3.0.6 on 2020-05-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produc', '0003_auto_20200517_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='summary',
            field=models.TextField(),
        ),
    ]
