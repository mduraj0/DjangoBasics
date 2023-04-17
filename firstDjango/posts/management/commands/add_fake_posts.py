from django.core.management.base import BaseCommand
from posts.utils import create_posts

class Command(BaseCommand):
    help = 'Create fake posts'

    def handle(self, *args, **options):
        create_posts(
            options.get('count')
        )
        self.stdout.write('Posts has been created!')

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '-- count',
            type=int,
            default=10,
            dest='count',
            help='Amount of posts to generate'
        )