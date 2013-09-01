from django.core.urlresolvers import reverse
from django.test import TestCase
from ..models import Article


class ArticleTest(TestCase):
    def test_get_absolute_url(self):
        article = Article(slug='spam-eggs')
        expected = reverse('article', kwargs={'slug': 'spam-eggs'})
        self.assertEqual(expected, article.get_absolute_url())
