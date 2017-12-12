# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import emencia.django.newsletter.models
import datetime
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file_attachment', models.FileField(upload_to=emencia.django.newsletter.models.get_newsletter_storage_path, max_length=255, verbose_name='file to attach')),
                ('contentType', models.CharField(blank=True, max_length=255, verbose_name='Content type', choices=[(0, b'image/x-cmu-raster (.ras)'), (1, b'application/x-shar (.shar)'), (2, b'image/x-ms-bmp (.bmp)'), (3, b'image/jpeg (.jpe,.jpg,.jpeg)'), (4, b'image/svg+xml (.svg)'), (5, b'application/postscript (.ai,.ps,.eps)'), (6, b'video/quicktime (.mov,.qt)'), (7, b'application/x-dvi (.dvi)'), (8, b'application/x-sh (.sh)'), (9, b'application/x-troff-me (.me)'), (10, b'image/x-xpixmap (.xpm)'), (11, b'application/x-texinfo (.texinfo,.texi)'), (12, b'text/xml (.xml)'), (13, b'application/x-latex (.latex)'), (14, b'image/ief (.ief)'), (15, b'image/x-portable-anymap (.pnm)'), (16, b'application/x-mif (.mif)'), (17, b'application/pdf (.pdf)'), (18, b'image/png (.png)'), (19, b'image/x-xbitmap (.xbm)'), (20, b'image/x-portable-bitmap (.pbm)'), (21, b'application/x-ustar (.ustar)'), (22, b'message/rfc822 (.mht,.nws,.eml,.mhtml)'), (23, b'text/x-setext (.etx)'), (24, b'application/x-hdf (.hdf)'), (25, b'application/x-troff (.tr,.t,.roff)'), (26, b'image/x-rgb (.rgb)'), (27, b'application/x-troff-ms (.ms)'), (28, b'image/gif (.gif)'), (29, b'application/javascript (.js)'), (30, b'application/zip (.zip)'), (31, b'video/webm (.webm)'), (32, b'application/xml (.wsdl,.xpdl,.rdf,.xsl)'), (33, b'application/vnd.ms-excel (.xlb,.xls)'), (34, b'application/pkcs7-mime (.p7c)'), (35, b'image/tiff (.tif,.tiff)'), (36, b'application/x-sv4crc (.sv4crc)'), (37, b'application/x-tar (.tar)'), (38, b'video/x-sgi-movie (.movie)'), (39, b'image/x-portable-graymap (.pgm)'), (40, b'application/x-pn-realaudio (.ram)'), (41, b'audio/x-pn-realaudio (.ra)'), (42, b'audio/mpeg (.mp3,.mp2)'), (43, b'audio/x-wav (.wav)'), (44, b'application/x-netcdf (.cdf,.nc)'), (45, b'application/oda (.oda)'), (46, b'image/vnd.microsoft.icon (.ico)'), (47, b'application/x-gtar (.gtar)'), (48, b'video/mp4 (.mp4)'), (49, b'application/octet-stream (.obj,.dll,.so,.exe,.bin,.o,.a)'), (50, b'text/x-vcard (.vcf)'), (51, b'image/x-portable-pixmap (.ppm)'), (52, b'application/x-sv4cpio (.sv4cpio)'), (53, b'text/plain (.ksh,.pl,.bat,.h,.c,.txt)'), (54, b'application/x-wais-source (.src)'), (55, b'application/x-pkcs12 (.p12,.pfx)'), (56, b'application/vnd.ms-powerpoint (.pwz,.ppt,.pps,.ppa,.pot)'), (57, b'text/tab-separated-values (.tsv)'), (58, b'application/x-tex (.tex)'), (59, b'text/x-python (.py)'), (60, b'image/x-xwindowdump (.xwd)'), (61, b'application/x-python-code (.pyc,.pyo)'), (62, b'application/x-cpio (.cpio)'), (63, b'application/x-bcpio (.bcpio)'), (64, b'text/html (.html,.htm)'), (65, b'video/mpeg (.m1v,.mpeg,.mpa,.mpg,.mpe)'), (66, b'text/richtext (.rtx)'), (67, b'text/x-sgml (.sgm,.sgml)'), (68, b'application/x-tcl (.tcl)'), (69, b'video/x-msvideo (.avi)'), (70, b'application/x-shockwave-flash (.swf)'), (71, b'text/csv (.csv)'), (72, b'audio/basic (.au,.snd)'), (73, b'audio/x-aiff (.aif,.aiff,.aifc)'), (74, b'application/x-csh (.csh)'), (75, b'application/x-troff-man (.man)'), (76, b'text/css (.css)'), (77, b'application/msword (.doc,.dot,.wiz)')])),
            ],
            options={
                'verbose_name': 'attachment',
                'verbose_name_plural': 'attachments',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='email')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=50, verbose_name='last name', blank=True)),
                ('subscriber', models.BooleanField(default=True, verbose_name='subscriber')),
                ('valid', models.BooleanField(default=True, verbose_name='valid email')),
                ('tester', models.BooleanField(default=False, verbose_name='contact tester')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='tags', blank=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ('creation_date',),
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='ContactMailingStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(verbose_name='status', choices=[(-1, 'sent in test'), (0, 'sent'), (1, 'error'), (2, 'invalid email'), (4, 'opened'), (5, 'opened on site'), (6, 'link opened'), (7, 'unsubscription'), (8, 'bounced'), (9, 'complaint'), (10, 'rejected')])),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('contact', models.ForeignKey(verbose_name='contact', to='newsletter.Contact')),
            ],
            options={
                'ordering': ('creation_date',),
                'verbose_name': 'contact mailing status',
                'verbose_name_plural': 'contact mailing statuses',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('url', models.CharField(max_length=255, verbose_name='url')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
            ],
            options={
                'ordering': ('creation_date',),
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
            },
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
                ('subscribers', models.ManyToManyField(related_name='mailinglist_subscriber', verbose_name='subscribers', to='newsletter.Contact')),
                ('unsubscribers', models.ManyToManyField(related_name='mailinglist_unsubscriber', null=True, verbose_name='unsubscribers', to='newsletter.Contact', blank=True)),
            ],
            options={
                'ordering': ('creation_date',),
                'verbose_name': 'mailing list',
                'verbose_name_plural': 'mailing lists',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(default='<body>\n<!-- Edit your newsletter here -->\n</body>', help_text='Or paste an URL.', verbose_name='content')),
                ('header_sender', models.CharField(default=b'Emencia Newsletter<noreply@emencia.com>', max_length=255, verbose_name='sender')),
                ('header_reply', models.CharField(default=b'Emencia Newsletter<noreply@emencia.com>', max_length=255, verbose_name='reply to')),
                ('status', models.IntegerField(default=0, verbose_name='status', choices=[(0, 'draft'), (1, 'waiting sending'), (2, 'sending'), (4, 'sent'), (5, 'canceled')])),
                ('sending_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='sending date')),
                ('slug', models.SlugField(help_text='Used for displaying the newsletter on the site.', unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='modification date')),
                ('mailing_list', models.ForeignKey(verbose_name='mailing list', to='newsletter.MailingList')),
            ],
            options={
                'ordering': ('creation_date',),
                'verbose_name': 'newsletter',
                'verbose_name_plural': 'newsletters',
                'permissions': (('can_change_status', 'Can change status'),),
            },
        ),
        migrations.CreateModel(
            name='SMTPServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('host', models.CharField(max_length=255, verbose_name='server host')),
                ('user', models.CharField(help_text='Leave it empty if the host is public.', max_length=128, verbose_name='server user', blank=True)),
                ('password', models.CharField(help_text='Leave it empty if the host is public.', max_length=128, verbose_name='server password', blank=True)),
                ('port', models.IntegerField(default=25, verbose_name='server port')),
                ('tls', models.BooleanField(verbose_name='server use TLS')),
                ('headers', models.TextField(help_text='key1: value1 key2: value2, splitted by return line.', verbose_name='custom headers', blank=True)),
                ('mails_hour', models.IntegerField(default=0, verbose_name='mails per hour')),
            ],
            options={
                'verbose_name': 'SMTP server',
                'verbose_name_plural': 'SMTP servers',
            },
        ),
        migrations.CreateModel(
            name='WorkGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('contacts', models.ManyToManyField(to='newsletter.Contact', null=True, verbose_name='contacts', blank=True)),
                ('group', models.ForeignKey(verbose_name='permissions group', to='auth.Group')),
                ('mailinglists', models.ManyToManyField(to='newsletter.MailingList', null=True, verbose_name='mailing lists', blank=True)),
                ('newsletters', models.ManyToManyField(to='newsletter.Newsletter', null=True, verbose_name='newsletters', blank=True)),
            ],
            options={
                'verbose_name': 'workgroup',
                'verbose_name_plural': 'workgroups',
            },
        ),
        migrations.AddField(
            model_name='newsletter',
            name='server',
            field=models.ForeignKey(default=1, verbose_name='smtp server', to='newsletter.SMTPServer'),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='test_contacts',
            field=models.ManyToManyField(to='newsletter.Contact', null=True, verbose_name='test contacts', blank=True),
        ),
        migrations.AddField(
            model_name='contactmailingstatus',
            name='link',
            field=models.ForeignKey(verbose_name='link', blank=True, to='newsletter.Link', null=True),
        ),
        migrations.AddField(
            model_name='contactmailingstatus',
            name='newsletter',
            field=models.ForeignKey(verbose_name='newsletter', to='newsletter.Newsletter'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='newsletter',
            field=models.ForeignKey(verbose_name='newsletter', to='newsletter.Newsletter'),
        ),
    ]
