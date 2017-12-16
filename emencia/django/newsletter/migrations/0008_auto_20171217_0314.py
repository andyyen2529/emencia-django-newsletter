# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('newsletter', '0007_auto_20171212_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='footerContentType',
            field=models.ForeignKey(related_name='newsletter_footer', blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='footerId',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='headerContentType',
            field=models.ForeignKey(related_name='newsletter_header', blank=True, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='headerId',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
