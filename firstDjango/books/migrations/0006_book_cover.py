# Generated by Django 4.1.4 on 2023-05-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/%Y/%m/%d'),
        ),
    ]