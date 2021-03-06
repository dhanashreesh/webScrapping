from django.core.management.base import BaseCommand, CommandError
from scraping.scraper import WebScraper
from django.core.cache import cache

class Command(BaseCommand):

	def handle(self, *args, **options):
		set_scraper_info()

def set_scraper_info():
	scraper = WebScraper()
	data = scraper.get_nifty_50_table()
	cache.set('nifty_50_table', data, timeout=None)