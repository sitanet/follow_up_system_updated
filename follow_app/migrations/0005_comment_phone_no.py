# Generated by Django 4.2.4 on 2023-09-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0004_alter_member_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='phone_no',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
