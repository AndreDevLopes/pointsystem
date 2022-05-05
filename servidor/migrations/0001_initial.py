# Generated by Django 4.0.4 on 2022-05-02 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('secretaria', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=15)),
                ('cargo', models.CharField(max_length=200)),
                ('secretaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secretaria.secretaria')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]