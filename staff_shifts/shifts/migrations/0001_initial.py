# Generated by Django 4.2.10 on 2024-02-22 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profiles', '0002_alter_availability_address_alter_availability_user_and_more'),
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_users', models.PositiveIntegerField(default=1)),
                ('shift_name', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('cancelled', 'Cancelled'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('reminder_enabled', models.BooleanField(default=False)),
                ('reminder_days_before', models.PositiveIntegerField(default=3)),
                ('employer_address_line1', models.CharField(blank=True, max_length=255, null=True)),
                ('employer_address_line2', models.CharField(blank=True, max_length=255, null=True)),
                ('employer_city', models.CharField(blank=True, max_length=255, null=True)),
                ('employer_state', models.CharField(blank=True, max_length=255, null=True)),
                ('employer_postal_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=20)),
                ('offer_message', models.TextField(blank=True, null=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers_sent', to='employers.employer')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.shift')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_offers_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_selected', models.DateTimeField()),
                ('is_available', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_availability', to='user_profiles.address')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shifts.shift')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_availability', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'date_time_selected')},
            },
        ),
    ]
