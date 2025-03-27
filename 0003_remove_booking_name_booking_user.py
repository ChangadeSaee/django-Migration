# Generated by Django 4.2.1 on 2023-05-07 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restaurant", "0002_booking_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="name",
        ),
        migrations.AddField(
            model_name="booking",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
