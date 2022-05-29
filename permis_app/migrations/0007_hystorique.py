# Generated by Django 3.2 on 2022-05-16 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permis_app', '0006_auto_20220516_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hystorique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=250)),
                ('datecon', models.CharField(max_length=250)),
                ('datedecon', models.CharField(max_length=250)),
                ('tmps', models.CharField(blank=True, max_length=250, null=True)),
                ('id_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
