# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

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


@login_required(login_url="/accounts/login")
def article_create(request):
	if request.method =='POST':
		form = forms.CreateArticle(request.POST,request.FILES)
		if forms.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()

			return redirect('article:list')
	else:
		form =forms.CreateArticle()
	return render(request,'articles/articles_create.html',{'form':form})
