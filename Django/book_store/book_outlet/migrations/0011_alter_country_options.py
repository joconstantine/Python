# Generated by Django 3.2.2 on 2021-05-30 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0010_alter_country_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
    ]