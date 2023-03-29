# Generated by Django 4.1.7 on 2023-03-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('min_salary', models.FloatField(blank=True, null=True)),
                ('max_salary', models.FloatField(blank=True, null=True)),
                ('skills', models.CharField(blank=True, max_length=255)),
                ('qualifications', models.TextField()),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
    ]