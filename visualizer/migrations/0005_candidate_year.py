# Generated by Django 3.1.3 on 2020-12-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0004_auto_20201210_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='year',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]
