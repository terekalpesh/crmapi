# Generated by Django 4.0.10 on 2024-07-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='document',
            field=models.FileField(default='documents/default_file.pdf', upload_to='media'),
        ),
    ]