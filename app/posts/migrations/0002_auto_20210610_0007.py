# Generated by Django 3.1.12 on 2021-06-10 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='picture_mobile',
            field=models.ImageField(blank=True, help_text='Automatically Generated. Dimensions: 100px(width) x 100px(height). Extension: png.', max_length=255, upload_to='', verbose_name='Picture Mobile'),
        ),
        migrations.AlterField(
            model_name='author',
            name='picture',
            field=models.ImageField(help_text='Minimum dimensions: 200px(width) x 200px(height). Extension: png.', upload_to='', verbose_name='Picture'),
        ),
    ]