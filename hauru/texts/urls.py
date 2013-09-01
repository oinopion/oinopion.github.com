import hurl

urlpatterns = hurl.patterns('hauru.texts.views', {
    '': 'article_list',
    '<slug>': 'article',
})
