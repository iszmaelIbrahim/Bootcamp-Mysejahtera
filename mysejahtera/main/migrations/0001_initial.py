# Generated by Django 3.2.5 on 2021-07-12 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='vaccine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=100)),
                ('age', models.CharField(default='NA', max_length=100)),
                ('state', models.CharField(choices=[('Selangor', 'Selangor'), ('Perak', 'Perak'), ('Pahang', 'Pahang'), ('Johor', 'Johor')], max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=300)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='location_qr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_code')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NA', max_length=100)),
                ('age', models.CharField(default='NA', max_length=100)),
                ('fever', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('Chills', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('headache', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('vomiting', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('diarrhea', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]