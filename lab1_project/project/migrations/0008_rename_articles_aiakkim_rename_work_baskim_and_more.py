# Generated by Django 4.0.2 on 2022-03-02 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_articles_content1_kumuz_content1_work_content1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Aiakkim',
        ),
        migrations.RenameModel(
            old_name='Work',
            new_name='Baskim',
        ),
        migrations.RenameModel(
            old_name='Kumuz',
            new_name='Surtkim',
        ),
    ]