from django.urls import path
from .views import index,get_category

urlpatterns = [
    path('', index, name="Home"),
    path('category/<int:category_id>/', get_category, name= 'category')
]