# Generated by Django 3.1.3 on 2022-06-09 20:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
