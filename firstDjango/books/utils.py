from faker import Faker
from .models import Book

fake = Faker('pl_PL')


def create_books(n=10):
    results = []
    for i in range(n):
        d = fake.date_time()
        p = Book.objects.create(
            title=fake.text(fake.random.randint(20, 80)),
            description=fake.text(fake.random.randint(200, 300)),
            publication_year=int(fake.year()),
            author=fake.name(),
            available=fake.boolean()
        )
    results.append(p)

    return results
