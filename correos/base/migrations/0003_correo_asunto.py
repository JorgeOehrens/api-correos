# Generated by Django 4.0.5 on 2022-06-02 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_corre_admin_correo_correo_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='correo',
            name='asunto',
            field=models.CharField(default='Recuperar contraseña', max_length=200),
            preserve_default=False,
        ),
    ]