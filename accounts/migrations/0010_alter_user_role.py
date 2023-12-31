# Generated by Django 4.2.4 on 2023-09-22 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Coordinator'), (3, 'Team Member'), (4, 'Pastor')], null=True),
        ),
    ]
