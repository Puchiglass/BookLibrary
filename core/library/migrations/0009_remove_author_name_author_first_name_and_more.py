# Generated by Django 4.2.5 on 2023-10-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='', help_text='имя', max_length=100),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='', help_text='фамилия', max_length=100),
        ),
        migrations.AddField(
            model_name='author',
            name='portrait',
            field=models.ImageField(blank=True, help_text='Portrait', upload_to='images/authors', verbose_name='portrait'),
        ),
        migrations.AddField(
            model_name='author',
            name='surename',
            field=models.CharField(blank=True, default='', help_text='отчество, если есть', max_length=100, null=True),
        ),
    ]
