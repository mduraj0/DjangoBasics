from django.core.management.base import BaseCommand
from books.utils import create_books


class Command(BaseCommand):
    help = 'creating fake books'

    def handle(self, *args, **options):
        create_books(
            options.get('number')
        )
        self.stdout.write('books was created')

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            "--number",
            type=int,
            default=10,
            dest="number",
            help="Amount of books"
        )
