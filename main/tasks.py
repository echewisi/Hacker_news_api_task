# tasks.py
from celery import shared_task
import requests
from .models import Story  # Replace 'myapp' with your actual app name

HACKER_NEWS_API_URL = "https://hacker-news.firebaseio.com/v0/"
TOP_STORIES_URL = f"{HACKER_NEWS_API_URL}topstories.json"
NEW_STORIES_URL = f"{HACKER_NEWS_API_URL}newstories.json"

@shared_task
def sync_hacker_news():
    top_stories = requests.get(TOP_STORIES_URL).json()
    new_stories = requests.get(NEW_STORIES_URL).json()

    for item_id in set(top_stories + new_stories):
        item_data = requests.get(f"{HACKER_NEWS_API_URL}item/{item_id}.json").json()

        news_item, created = Story.objects.get_or_create(
            hn_id=item_id,
            defaults={
                'title': item_data.get('title', ''),
                'url': item_data.get('url', ''),
                # Add other fields as needed
            }
        )

        if created:
            print(f"Synced new item: {news_item.title}")
