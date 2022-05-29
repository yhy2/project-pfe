# Generated by Django 3.2 on 2022-05-16 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permis_app', '0004_auto_20220515_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomSociete', models.CharField(max_length=250)),
                ('dateInfraction', models.DateTimeField()),
                ('descInfraction', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Permis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypePermis', models.CharField(max_length=250)),
                ('dateDeDelivrance', models.DateTimeField()),
                ('etatRetrait', models.CharField(max_length=250)),
                ('dateExpiration', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Travailleur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomPrenom', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('numTel', models.CharField(max_length=250, unique=True)),
                ('numPass', models.CharField(max_length=250, unique=True)),
                ('dateNaissance', models.DateTimeField()),
                ('Nationalite', models.CharField(max_length=250)),
                ('descPoste', models.CharField(max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo')),
                ('id_Infra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='permis_app.infraction')),
                ('id_permis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='permis_app.permis')),
                ('id_soc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='permis_app.societe')),
            ],
        ),
    ]
