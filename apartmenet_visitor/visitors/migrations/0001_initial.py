# Generated by Django 4.0.6 on 2022-08-01 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('members', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=100, null=True)),
                ('wing', models.CharField(max_length=100)),
                ('floor', models.IntegerField()),
                ('number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service_images/')),
                ('phone', models.CharField(max_length=100)),
                ('identity', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=100, null=True)),
                ('flat', models.ManyToManyField(to='visitors.flat')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('identity', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departed_at', models.DateTimeField(blank=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors.flat')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departed_at', models.DateTimeField(blank=True)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors.flat')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors.serviceperson')),
            ],
        ),
        migrations.AddField(
            model_name='serviceperson',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors.servicetype'),
        ),
    ]
