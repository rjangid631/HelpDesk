# Generated by Django 5.1.7 on 2025-04-23 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='TaskID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Management.taskinformation'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='UserID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='Management.users'),
        ),
    ]
