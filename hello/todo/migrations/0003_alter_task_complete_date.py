# Generated by Django 3.2.5 on 2022-01-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20220120_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Task complete date'),
        ),
    ]
