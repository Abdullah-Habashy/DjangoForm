# Generated by Django 4.0.3 on 2022-03-24 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_rename_mail_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
    ]