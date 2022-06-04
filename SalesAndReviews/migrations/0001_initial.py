# Generated by Django 4.0.5 on 2022-06-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrugReview',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('condition', models.TextField()),
                ('date', models.DateField()),
                ('drugName', models.TextField()),
                ('rating', models.IntegerField()),
                ('review', models.TextField()),
                ('uniqueId', models.BigIntegerField()),
                ('usefulCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PharmaSales',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('m01ab', models.FloatField()),
                ('m01ae', models.FloatField()),
                ('n02ba', models.FloatField()),
                ('n02be', models.FloatField()),
                ('n05b', models.FloatField()),
                ('n05c', models.FloatField()),
                ('r03', models.FloatField()),
                ('r06', models.FloatField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
