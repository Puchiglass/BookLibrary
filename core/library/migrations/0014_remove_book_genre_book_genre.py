# Generated by Django 4.2.5 on 2023-10-06 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_alter_book_options_remove_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='genre', null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.genre'),
        ),
    ]
