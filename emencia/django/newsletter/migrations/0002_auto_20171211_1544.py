# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ('creation_date',), 'verbose_name': 'newsletter', 'verbose_name_plural': 'newsletters', 'permissions': (('can_change_status', '\u53ef\u6539\u8b8a\u72c0\u614b'),)},
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='content',
            field=models.TextField(default='<body>\n<!-- \u5728\u9019\u88e1\u7de8\u8f2f\u4f60\u7684\u96fb\u5b50\u5831 -->\n</body>', help_text='Or paste an URL.', verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='header_reply',
            field=models.CharField(default=b'Nuwa<service@tracedig.com>', max_length=255, verbose_name='reply to'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='header_sender',
            field=models.CharField(default=b'Nuwa<service@tracedig.com>', max_length=255, verbose_name='sender'),
        ),
    ]
