# Generated by Django 2.0.7 on 2018-07-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
