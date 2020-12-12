# Generated by Django 3.1.3 on 2020-12-11 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0005_candidate_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='beginning_cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='ending_cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='total_donation_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='total_ind_contrib',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='total_spent_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
