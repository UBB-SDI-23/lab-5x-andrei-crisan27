# Generated by Django 4.1.7 on 2023-03-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individuals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('nationality', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('job', models.CharField(max_length=50)),
            ],
        ),
    ]
