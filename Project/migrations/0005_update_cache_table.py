# Generated by Django 4.2.4 on 2023-11-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_update_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update_cache_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_id', models.IntegerField(unique=True, verbose_name='project id')),
                ('upd_id', models.IntegerField(unique=True, verbose_name='updation_id')),
            ],
        ),
    ]
