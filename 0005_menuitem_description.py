# Generated by Django 5.1.5 on 2025-01-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_rename_menu_menuitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
