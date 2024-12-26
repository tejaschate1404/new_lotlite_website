# Generated by Django 5.0.6 on 2024-06-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_images/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('what_you_learn', models.TextField()),
                ('courses_included', models.TextField()),
                ('course_contents', models.TextField()),
                ('detailed_description', models.TextField()),
            ],
        ),
    ]
