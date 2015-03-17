# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjsonb.fields
import decimal
import django.core.serializers.json


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DummyData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_of_people', models.PositiveIntegerField()),
                ('budget', models.DecimalField(max_digits=10, decimal_places=2)),
                ('meta', django_pgjsonb.fields.JSONField(default={}, null=True, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
            ],
        ),
    ]
