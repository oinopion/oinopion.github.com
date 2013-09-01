from django.views.generic import DetailView, ListView
from .models import Article


class ArticleView(DetailView):
    model = Article
    context_object_name = 'article'


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'


article = ArticleView.as_view()
article_list = ArticleListView.as_view()
