# Generated by Django 5.0.4 on 2024-04-22 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_nomine_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nomine_nid_picture',
            field=models.ImageField(blank=True, upload_to='nomine_nidpicture/'),
        ),
    ]