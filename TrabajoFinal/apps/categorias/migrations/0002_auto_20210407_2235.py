# Generated by Django 3.0 on 2021-04-08 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='redaccion',
            options={'ordering': ['-fecha']},
        ),
    ]