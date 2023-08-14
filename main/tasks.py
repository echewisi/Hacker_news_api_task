from core.celery import app as celery_app
from celery import shared_task
import requests
from .models import Story
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


HACKER_NEWS_API_URL = "https://hacker-news.firebaseio.com/v0/"
TOP_STORIES_URL = f"{HACKER_NEWS_API_URL}topstories.json"
NEW_STORIES_URL = f"{HACKER_NEWS_API_URL}newstories.json"

@shared_task
def sync_hacker_news(last_item_id=None):
    if last_item_id is None:
        last_item = Story.objects.order_by('-id').first()
        last_item_id = last_item.id if last_item else 0
    
    top_stories = requests.get(TOP_STORIES_URL).json()
    new_stories = requests.get(NEW_STORIES_URL).json()

    items_to_sync = sorted(set(top_stories + new_stories) - set(range(last_item_id)))

    if last_item_id == 0:
        # Sync the first 100 stories initially
        items_to_sync = items_to_sync[:100]

    for item_id in items_to_sync:
        item_data = requests.get(f"{HACKER_NEWS_API_URL}item/{item_id}.json").json()

        news_item, created = Story.objects.get_or_create(
            id=item_id,
            defaults={
                'author': item_data.get('by', ''),
                'score': item_data.get('score', 0),
                'title': item_data.get('title', ''),
                'url': item_data.get('url', ''),
            }
        )
        
        if created:
            logger.info(f"Synced new item: {news_item.title}")
