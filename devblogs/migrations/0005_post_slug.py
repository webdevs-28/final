# Generated by Django 4.2.2 on 2023-08-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devblogs', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]
