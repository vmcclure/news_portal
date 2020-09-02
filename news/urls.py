from django.urls import path
from .views import index,get_category, view_news, add_news, HomeNews

urlpatterns = [
    path('', index, name="Home"),
    path('', HomeNews.as_view(), name="Home"),
    path('category/<int:category_id>/', get_category, name= 'category'),
    path('news/<int:news_id>/', view_news, name= 'view_news'),
    path('news/add_news/', add_news, name= 'add_news'),
]