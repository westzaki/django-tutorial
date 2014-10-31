# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='name', max_length=255)),
                ('publisher', models.CharField(verbose_name='publisher', blank=True, max_length=255)),
                ('page', models.IntegerField(verbose_name='page', default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Impression',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('comment', models.TextField(verbose_name='comment', blank=True)),
                ('book', models.ForeignKey(related_name='impressions', verbose_name='book', to='cms.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
