from django.core.urlresolvers import reverse
from django.test import TestCase
from ..models import Article


class ArticleTest(TestCase):
    def test_get_absolute_url(self):
        article = Article(slug='spam-eggs')
        expected = reverse('article_detail', kwargs={'slug': 'spam-eggs'})
        self.assertEqual(expected, article.get_absolute_url())

    def test_signed_id(self):
        article = Article(pk=1, slug='spam-eggs')
        signed_id = article.signed_id()
        self.assertEqual(str(article.pk), signed_id[0])

    def test_is_signed_id(self):
        article = Article(pk=1, slug='spam-eggs')
        self.assertFalse(article.is_signed_id("1"))

        signed_id = article.signed_id()
        self.assertTrue(article.is_signed_id(signed_id))
