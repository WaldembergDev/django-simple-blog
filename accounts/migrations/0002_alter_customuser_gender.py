# Generated by Django 5.2 on 2025-04-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Masculine'), ('F', 'Feminine')], max_length=10, null=True),
        ),
    ]
