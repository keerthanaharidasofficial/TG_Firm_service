# Generated by Django 4.2.7 on 2024-01-02 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0002_rename_name_role_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_app.department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_app.role'),
        ),
    ]
