from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Story, Profile
from django.db.models import Q
from .forms import ProfileForm, StoryUpdateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


@login_required
def profile(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(id=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'form': form})

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

def top_level_items(request):
    top_items = Story.objects.filter(parent=None)
    return render(request, 'top_level_items.html', {'top_items': top_items})

def item_detail(request, item_id):
    item = get_object_or_404(Story, id=item_id)
    children = item.children.all()
    return render(request, 'item_detail.html', {'item': item, 'children': children})



@login_required
def update_item(request, item_id):
    item = get_object_or_404(Story, id=item_id, api_created=True)
    
    if request.method == 'POST':
        # Handle form submission and update item data
        form = StoryUpdateForm(request.POST, instance=item)
        if form.is_valid():
            updated_item = form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return render(request, 'update_item.html', {'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Story, id=item_id, api_created=True)
    
    if request.method == 'POST':
        # Delete the item
        item.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})


# Create your views here.
