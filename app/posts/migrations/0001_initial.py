# Generated by Django 3.1.12 on 2021-06-08 03:01

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('picture', models.ImageField(help_text='Minimum dimensions: 300px(width) x 300px(heigth). Extension: jpg.', upload_to='', verbose_name='Picture')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Update at')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'db_table': 'tb_author',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('category', models.CharField(max_length=255, verbose_name='Category')),
                ('summary', models.CharField(max_length=510, verbose_name='Summary')),
                ('first_paragraph', ckeditor.fields.RichTextField(verbose_name='First Paragraph')),
                ('body', ckeditor.fields.RichTextField(verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Update at')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.author', verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'db_table': 'tb_article',
            },
        ),
    ]
