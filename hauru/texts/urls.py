import hurl

urlpatterns = hurl.patterns('hauru.texts.views', {
    '': 'article_list',
    '<slug>': 'article_detail',
    '<slug>/<signature:str>': 'article_preview',
})
