"""Command for sending the newsletter"""
from django.core.management.base import BaseCommand

from emencia.django.newsletter.mailer import Mailer
from emencia.django.newsletter.models import Newsletter


class Command(BaseCommand):
    """Send the newsletter in queue"""
    help = 'Send the newsletter in queue'

    def handle(self, *args, **options):
        verbose = int(options['verbosity'])

        if verbose:
            print('Starting sending newsletters...')

        for newsletter in Newsletter.objects.exclude(
            status=Newsletter.DRAFT).exclude(status=Newsletter.SENT):
            mailer = Mailer(newsletter)
            if mailer.can_send:
                if verbose:
                    print('Start emailing %s' % newsletter.title)
                mailer.run()

        if verbose:
            print('End session sending')
