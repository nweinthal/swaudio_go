# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reservation_name', models.CharField(max_length=500)),
                ('swatmail', models.EmailField(max_length=75)),
                ('class_year', models.IntegerField()),
                ('best_contact_method', models.CharField(max_length=100)),
                ('other_contact_method', models.CharField(max_length=500, null=True, blank=True)),
                ('pickup_date', models.DateField()),
                ('dropoff_date', models.DateField()),
                ('request_submitted', models.DateTimeField(editable=False)),
                ('group', models.CharField(max_length=500, null=True, blank=True)),
                ('additional_equipment', models.ManyToManyField(to='inventory.Item', null=True)),
                ('approver', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
                ('assigned_system', models.ForeignKey(to='inventory.System', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField()),
                ('placed_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('system', models.ForeignKey(to='inventory.System')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
