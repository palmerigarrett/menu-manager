# Generated by Django 3.0.8 on 2020-07-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dishTitle', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(max_length=100)),
                ('created', models.DateField(default='2020-07-14')),
            ],
            options={
                'ordering': ['dishTitle'],
            },
        ),
    ]