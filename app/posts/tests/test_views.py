from django.test import TestCase

from posts.models import Author, Article

from django.core.files.uploadedfile import SimpleUploadedFile


class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(
            name='Eduardo Monita Dias', 
            picture=SimpleUploadedFile(name='test_edu.jpg', 
                content=open('/app/edu.jpg', 'rb').read(), 
                content_type='image/jpeg'), 
            active=True
        )
        Author.objects.create(
            name='Ana Carolina de Matos Brunetti', 
            picture=SimpleUploadedFile(name='test_ana.jpg', 
                content=open('/app/ana.jpg', 'rb').read(), 
                content_type='image/jpeg'), 
            active=True)

        Article.objects.create(
            author=Author.objects.filter(name='Eduardo Monita Dias').first(),
            title='Title 1', 
            category='Category 1', 
            summary='Summary 1', 
            first_paragraph='<p>first_paragraph 1</p>',
            body='<p>body 1</p>'
        )
        Article.objects.create(
            author=Author.objects.filter(name='Ana Carolina de Matos Brunetti').first(),
            title='Title 2', 
            category='Category 2', 
            summary='Summary 2', 
            first_paragraph='<p>first_paragraph 2</p>',
            body='<p>body 2</p>'
        )

    def test_index_loads_properly(self):
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)

    def test_articles_detail(self):
        article = Article.objects.all().first()
        response = self.client.get(f'/api/articles/{article.id}/')
        self.assertEqual(response.status_code, 200)

    def test_articles_list(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
