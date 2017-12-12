# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20171212_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='subject',
            field=models.CharField(default=b'This is subject.', max_length=255, verbose_name='subject'),
        ),
    ]
