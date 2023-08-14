from django.urls import path
from . import views

app_name= 'main'

urlpatterns = [
    path('latest-news/', views.latest_news, name='latest_news'),
    path('latest-news/?type=type1', views.latest_news, name= 'latest_news_items'),
    path('latest-news/?query=search_query', views.latest_news, name= 'latest_news_query'),
    path('latest-news/?type=type1&q=search_query', views.latest_news, name= "latest_news_combine"),
    path('items/', views.top_level_items, name='top_level_items'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('item/<int:item_id>/update/', views.update_item, name='update_item'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),


]