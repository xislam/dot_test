# Generated by Django 4.0 on 2021-12-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_for_bot', '0003_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='apidata',
            name='sent',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
