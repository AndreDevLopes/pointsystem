# Generated by Django 4.0.4 on 2022-07-17 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('feriado', '0005_alter_feriado_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feriado',
            name='endereco',
            field=models.ManyToManyField(blank=True, default='feriado en todo territorio <django.db.models.fields.CharField>', to='endereco.cidade'),
        ),
    ]
