# Generated by Django 4.0.6 on 2022-10-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]