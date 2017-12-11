# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20171211_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='subjectTitle',
            field=models.CharField(max_length=255, null=True, verbose_name='subject title', blank=True),
        ),
    ]
