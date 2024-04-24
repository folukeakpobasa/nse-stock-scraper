import os
from dotenv import load_dotenv

load_dotenv()
BOT_NAME = 'nse_scraper'

SPIDER_MODULES = ['nse_scraper.spiders']
NEWSPIDER_MODULE = 'nse_scraper.spiders'

# MONGODB SETTINGS
MONGODB_URI = os.getenv("MONGODB_URI")
MONGO_DATABASE = os.getenv("MONGO_DATABASE")

ITEM_PIPELINES = {
   'nse_scraper.pipelines.NseScraperPipeline': 300,
}
LOG_LEVEL = "INFO"

# USER_AGENT = 'nse_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Accept-Language': 'en',
}

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 360
HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'