# Generated by Django 3.0 on 2021-03-16 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0006_remove_redacción_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redacción',
            name='fecha',
        ),
    ]
