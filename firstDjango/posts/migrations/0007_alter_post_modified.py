# Generated by Django 4.1.4 on 2023-04-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_category_post_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
