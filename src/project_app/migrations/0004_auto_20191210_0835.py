# Generated by Django 2.0.9 on 2019-12-10 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0003_auto_20191210_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project_project', to='project_app.Project'),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_project_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
