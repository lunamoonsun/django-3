# Generated by Django 3.0 on 2023-12-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Tecnologia'), ('CR', 'Curiosidade'), ('GR', 'Geral')], default='GR', max_length=2),
        ),
    ]
