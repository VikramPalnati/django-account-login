
from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
 
    url(r'^articles/$',views.article_list,name="list"),
    url(r'^(?P<slug>[\w-]+)/$',views.articles_detail,name="detail"),
    url(r'^creates/$',views.article_create,name='create'),
    
]
