# Generated by Django 2.2.24 on 2021-08-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0036_add_license_duration_before_purge_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeragreement',
            name='enterprise_customer_slug',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='historicalcustomeragreement',
            name='enterprise_customer_slug',
            field=models.CharField(blank=True, db_index=True, max_length=128, null=True),
        ),
    ]