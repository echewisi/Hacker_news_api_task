from celery import shared_task
from core.celery import app as celery_app
from datetime import timedelta
from celery.task import periodic_task
import requests
from .models import Story

HACKER_NEWS_API_URL = "https://hacker-news.firebaseio.com/v0/"
TOP_STORIES_URL = f"{HACKER_NEWS_API_URL}topstories.json"
NEW_STORIES_URL = f"{HACKER_NEWS_API_URL}newstories.json"

@periodic_task(run_every=timedelta(minutes=5))
def sync_hacker_news():
    top_stories = requests.get(TOP_STORIES_URL).json()[:100]  # Fetch the first 100 stories
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
