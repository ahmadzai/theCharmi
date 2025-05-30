# Generated by Django 4.2.20 on 2025-05-02 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0002_contactinquiry_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinquiry',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contact_inquiries_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]
