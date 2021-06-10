from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Author(models.Model):

    name = models.CharField('Name', max_length=255)
    picture = models.ImageField('Picture', help_text='Minimum dimensions: 200px(width) x 200px(height). Extension: png.')
    picture_mobile = models.ImageField('Picture Mobile', help_text='Automatically Generated. Dimensions: 100px(width) x 100px(height). Extension: png.', max_length=255, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Update at', auto_now_add=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        db_table = 'tb_author'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.name}'

class Article(models.Model):

    title = models.CharField('Title', max_length=255)
    category = models.CharField('Category', max_length=255)
    summary = models.CharField('Summary', max_length=510)
    first_paragraph = RichTextField('First Paragraph')
    body = RichTextField('Body')

    author = models.ForeignKey(Author, verbose_name='Author', on_delete=models.PROTECT)

    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Update at', auto_now_add=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        db_table = 'tb_article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.title}'
