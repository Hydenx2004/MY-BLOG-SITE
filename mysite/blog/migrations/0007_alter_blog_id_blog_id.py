# Generated by Django 5.0.2 on 2024-04-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_id',
            name='Blog_Id',
            field=models.IntegerField(),
        ),
    ]