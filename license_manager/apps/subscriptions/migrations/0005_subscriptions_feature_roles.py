# Generated by Django 2.2.13 on 2020-06-15 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields

from license_manager.apps.subscriptions.constants import SUBSCRIPTIONS_ADMIN_ROLE


def create_roles(apps, schema_editor):
    """
    Create the enterprise subscriptions roles if they do not already exist.
    """
    SubscriptionsFeatureRole = apps.get_model('subscriptions', 'SubscriptionsFeatureRole')
    SubscriptionsFeatureRole.objects.update_or_create(name=SUBSCRIPTIONS_ADMIN_ROLE)


def delete_roles(apps, schema_editor):
    """
    Delete the enterprise subscriptions roles.
    """
    SubscriptionsFeatureRole = apps.get_model('subscriptions', 'SubscriptionsFeatureRole')
    SubscriptionsFeatureRole.objects.filter(name=SUBSCRIPTIONS_ADMIN_ROLE).delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0004_add_title_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionsFeatureRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionsRoleAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('enterprise_customer_uuid', models.UUIDField(blank=True, null=True, verbose_name='Enterprise Customer UUID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.SubscriptionsFeatureRole')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(create_roles, delete_roles),
    ]