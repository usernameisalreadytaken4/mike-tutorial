from django.conf.urls import include, url
from articles import views
from .api import ArticleResource

article_resource = ArticleResource()


urlpatterns = [
    url(r'^all/$', views.articles),
    url(r'^get/(?P<article_id>\d+)/$', views.article),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    url(r'^create/$', views.create),
    url(r'^like/(?P<article_id>\d+)/$', views.like_article),
    url(r'^add_comment/(?P<article_id>\d+)/$', views.add_comment),
    url(r'^delete_comment/(?P<comment_id>\d+)/$', views.delete_comment),
    url(r'^search/$', views.search_titles),
    url(r'^api/', include(article_resource.urls)),
]