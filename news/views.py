from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.shortcuts import get_object_or_404,redirect
from .forms import NewsForm
from django.views.generic import ListView
# Create your views here.

class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    # extra_context = {'title': 'главная'}
    def get_context_data(self, *, object_list=None, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title'] = 'главная'
        return context
    def get_queryset(self):
        return News.objects.filter(is_published=True)
def index(request):
    news = News.objects.order_by('-create_at')

    return render(request, 'news/index.html', {'news' : news,
                                               'title' : 'Список новостей',
                                               })


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news' : news,
                                               'category' : category,})

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)

    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method=="POST":
        form  = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form' : form})

