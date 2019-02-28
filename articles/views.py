# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.

def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render(request,'articles/articles_list.html',{'articles':articles})


def articles_detail(request,slug):
	#return HttpResponse(slug)
	try:
		article =Article.objects.get(slug=slug)
	except Article.DoesNotExist:
		article = None
	return render(request,'articles/articles_detail.html',{'article':article})