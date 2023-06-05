# Generated by Django 3.2.16 on 2022-11-28 16:56

from django.db import migrations, models
import django.db.models.deletion
import django_lifecycle.mixins
import pulpcore.app.models.base


class Migration(migrations.Migration):

    dependencies = [
        ('deb', '0022_alter_aptdistribution_distribution_ptr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptrepository',
            name='signing_service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='deb.aptreleasesigningservice'),
        ),
        migrations.CreateModel(
            name='AptRepositoryReleaseServiceOverride',
            fields=[
                ('pulp_id', models.UUIDField(default=pulpcore.app.models.base.pulp_uuid, editable=False, primary_key=True, serialize=False)),
                ('pulp_created', models.DateTimeField(auto_now_add=True)),
                ('pulp_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('release_distribution', models.TextField()),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signing_service_release_overrides', to='deb.aptrepository')),
                ('signing_service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='deb.aptreleasesigningservice')),
            ],
            options={
                'unique_together': {('repository', 'release_distribution')},
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]