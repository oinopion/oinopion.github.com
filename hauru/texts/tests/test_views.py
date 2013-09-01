from django.test import TestCase
from .factories import ArticleFactory


class ArticleViewTest(TestCase):
    def url(self, article):
        return '/texts/%s/' % article.slug

    def test_renders_template(self):
        article = ArticleFactory.create()
        resp = self.client.get(self.url(article))
        self.assertEqual(200, resp.status_code)
        self.assertTemplateUsed(resp, 'texts/article_detail.html')
        self.assertIn('article', resp.context)


class ArticleListViewTest(TestCase):
    def url(self):
        return '/texts/'

    def test_renders_template(self):
        ArticleFactory.create()
        resp = self.client.get(self.url())
        self.assertEqual(200, resp.status_code)
        self.assertTemplateUsed(resp, 'texts/article_list.html')
        self.assertIn('articles', resp.context)
