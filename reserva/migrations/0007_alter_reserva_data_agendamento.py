# Generated by Django 4.2.1 on 2023-06-20 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0006_alter_reserva_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_agendamento',
            field=models.DateTimeField(default=None, help_text='dd/mm/aaaa', verbose_name='Data'),
        ),
    ]
