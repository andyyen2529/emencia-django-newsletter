# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

def setDefaultSubjectTitles(apps, schema_editor):
    Newsletter = apps.get_model("newsletter", "Newsletter")
    for newsletter in Newsletter.objects.all():
        newsletter.subjectTitle = newsletter.title
        newsletter.save()

class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20171212_1004'),
    ]

    operations = [
        migrations.RunPython(setDefaultSubjectTitles),
        migrations.RenameField(
            model_name='newsletter',
            old_name='subjectTitle',
            new_name='subject',
        ),
    ]
