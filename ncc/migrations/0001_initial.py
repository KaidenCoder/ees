# Generated by Django 3.0.2 on 2020-01-17 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NCC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ncc/')),
                ('date', models.DateField()),
                ('headerline', models.CharField(default='', max_length=500)),
            ],
            options={
                'verbose_name': 'NCC',
                'verbose_name_plural': 'NCC',
            },
        ),
    ]
