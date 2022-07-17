# Generated by Django 4.0.4 on 2022-07-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feriados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('tipo', models.CharField(choices=[('NAC', 'Nacional'), ('EST', 'Estadual'), ('MUN', 'Municipal'), ('FAC', 'Facultativo')], default=None, max_length=3)),
            ],
        ),
    ]
