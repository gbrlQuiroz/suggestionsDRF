# Generated by Django 3.1.13 on 2021-12-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=9)),
            ],
            options={
                'db_table': 'cities',
                'ordering': ['id'],
            },
        ),
    ]
