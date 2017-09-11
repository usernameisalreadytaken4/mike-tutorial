from django.shortcuts import render, render_to_response
from articles.models import Article, Comment
from django.http import HttpResponse
from .forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.utils import timezone
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
from django.conf import settings
from django.contrib import messages
from django.template import RequestContext


import logging


logr = logging.getLogger(__name__)


def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))

    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render(request, 'articles.html', args)


def article(request, article_id=1):
    return render(request, 'article.html', {'article': Article.objects.get(id=article_id)})


def language(request, language='en-gb'):
    response = HttpResponse('setting language to %s' % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You Article was added')
            return HttpResponseRedirect('/articles/all')

    args = {}
    args.update(csrf(request))
    args['form'] = ArticleForm()
    return render(request, 'create_article.html', args)


def like_article(request, article_id=1):
    if article_id:
        a = Article.objects.get(id=article_id)
        a.likes += 1
        a.save()

    return HttpResponseRedirect('/articles/get/%s/' % article_id)


def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)

    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()

            messages.success(request, 'you comment was added')

            return HttpResponseRedirect('/articles/get/%s' % article_id)

    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = CommentForm()

    return render(request, 'add_comment.html', args)


def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    article_id = c.article.id
    c.delete()
    messages.add_message(request, settings.DELETE_MESSAGE, 'You comment was deleted')
    return HttpResponseRedirect('/articles/get/%s' % article_id)


def search_titles(request):

    if request.method == 'POST':
        search_text = request.POST['search_text']
        logr.debug(request.method)
    else:
        search_text = ''

    articles = Article.objects.filter(title__contains=search_text)
    logr.debug(articles)

    return render(request, 'ajax_search.html', {'articles': articles})
