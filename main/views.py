from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Story
from django.db.models import Q

def latest_news(request):
    item_type= request.GET.get('type') #to get the 'type'
    search_query = request.GET.get('q')    
    latest_items= Story.objects.order_by('-time')[:10]
    
    if item_type:
        latest_items= latest_items.filter(type= item_type)
    
    if search_query:
        latest_items= latest_items.filter(Q(title__icontains= search_query) | Q(content__icontains=search_query))
    
    paginator = Paginator(latest_items, per_page=10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        "page_obj": page_obj,
        "search_keyword": search_query,
        "item_type": item_type,
        "latest_news": latest_items
    }
    
    return render(request, 'latest_news.html', context)



    

# Create your views here.
