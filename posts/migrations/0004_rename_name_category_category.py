# Generated by Django 4.0.10 on 2024-07-12 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_rename_category_name_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
    ]
