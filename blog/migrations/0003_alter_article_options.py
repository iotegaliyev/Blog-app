# Generated by Django 4.2.4 on 2023-08-17 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_task_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('created',), 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
    ]
