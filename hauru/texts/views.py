from django.views.generic import DetailView, ListView
from .models import Article


class ArticleView(DetailView):
    queryset = Article.published.all()
    context_object_name = 'article'


class ArticleListView(ListView):
    queryset = Article.published.all()
    context_object_name = 'articles'


article = ArticleView.as_view()
article_list = ArticleListView.as_view()
