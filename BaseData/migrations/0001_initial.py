# Generated by Django 4.2.7 on 2023-11-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=10)),
                ('console', models.IntegerField()),
                ('single', models.IntegerField()),
                ('wt', models.IntegerField()),
            ],
        ),
    ]
