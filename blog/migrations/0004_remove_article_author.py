# Generated by Django 4.2.4 on 2023-08-17 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
