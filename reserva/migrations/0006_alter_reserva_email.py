# Generated by Django 4.2.1 on 2023-06-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0005_alter_reserva_data_agendamento_alter_reserva_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=50, verbose_name='E-mail'),
        ),
    ]
