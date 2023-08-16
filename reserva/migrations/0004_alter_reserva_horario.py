# Generated by Django 4.2.1 on 2023-06-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0003_remove_reserva_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='horario',
            field=models.CharField(choices=[('Indiferente', 'Indiferente'), ('Manhã', 'Manhã'), ('Tarde', 'Tarde')], default='Indiferente', max_length=30, verbose_name='Horário:'),
        ),
    ]