# Generated by Django 2.0.9 on 2020-03-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0004_auto_20191210_0835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-created',), 'permissions': (('view_project', 'View Project'),)},
        ),
    ]
