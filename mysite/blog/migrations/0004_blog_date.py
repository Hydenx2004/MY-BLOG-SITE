# Generated by Django 5.0.2 on 2024-04-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_author_id_blog_blog_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
