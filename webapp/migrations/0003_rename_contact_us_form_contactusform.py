# Generated by Django 5.1.4 on 2024-12-18 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_contactus_contact_us_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact_us_form',
            new_name='ContactUsForm',
        ),
    ]