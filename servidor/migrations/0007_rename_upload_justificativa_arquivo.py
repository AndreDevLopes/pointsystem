# Generated by Django 4.0.4 on 2022-06-12 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0006_justificativa_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='justificativa',
            old_name='upload',
            new_name='arquivo',
        ),
    ]
