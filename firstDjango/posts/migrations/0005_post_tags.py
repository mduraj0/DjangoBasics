# Generated by Django 4.1.4 on 2023-04-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('posts', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='tags.tag'),
        ),
    ]
