# Generated by Django 3.2.2 on 2021-05-30 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0009_auto_20210530_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=2),
        ),
    ]
