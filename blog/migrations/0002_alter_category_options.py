# Generated by Django 4.2.4 on 2023-09-07 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created'], 'verbose_name': 'categoría', 'verbose_name_plural': 'categorías'},
        ),
    ]
