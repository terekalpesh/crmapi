# Generated by Django 4.0.10 on 2024-07-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_category_category_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]