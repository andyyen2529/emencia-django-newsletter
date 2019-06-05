# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20171211_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='subjectTitle',
            field=models.CharField(max_length=255, null=True, verbose_name='subject title', blank=True),
        ),
    ]
