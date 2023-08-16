# Generated by Django 4.2.1 on 2023-06-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('nome_pet', models.CharField(max_length=50, verbose_name='Nome do Pet:')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('email', models.CharField(max_length=50, verbose_name='E-mail')),
                ('data_agendamento', models.CharField(max_length=11)),
                ('horario', models.CharField(choices=[('Indiferente', 'Indiferente'), ('07:00 as 08:00', '07:00 as 08:00'), ('08:00 as 09:00', '08:00 as 09:00'), ('09:00 as 10:00', '09:00 as 10:00'), ('10:00 as 11:00', '10:00 as 11:00'), ('11:00 as 12:00', '11:00 as 12:00'), ('13:00 as 14:00', '13:00 as 14:00'), ('14:00 as 15:00', '14:00 as 15:00'), ('15:00 as 16:00', '15:00 as 16:00'), ('16:00 as 17:00', '16:00 as 17:00'), ('17:00 as 18:00', '17:00 as 18:00')], default=None, max_length=30, verbose_name='Horário:')),
                ('tamanho', models.CharField(choices=[('Pequeno', 'Pequeno'), ('Pequeno', 'Medio'), ('Grande', 'Grande')], default=None, max_length=10, verbose_name='Tamanho: ')),
                ('levaetraz', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default=None, max_length=3, verbose_name='Precisa de Transtorte? ')),
                ('observacao', models.TextField(blank=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Reserva de Banho',
                'verbose_name_plural': 'Reservas de Banhos',
            },
        ),
    ]