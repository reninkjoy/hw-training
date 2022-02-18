from datetime import datetime
now = datetime.now()
day = int(now.strftime("%d"))

db_month = now
new_format = "%Y_%m"
db_date = db_month.strftime(new_format)
dbname = 'kw_monthly_' + db_date
BOT_NAME = 'haraj'

SPIDER_MODULES = ['haraj.spiders']
NEWSPIDER_MODULE = 'haraj.spiders'
DUP_KEY = ''
USER_AGENT = "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36"

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = dbname
MONGO_COLLECTION = 'haraj_data'
MONGO_COLLECTION_URL = 'haraj_urls'
DOWNLOADER_MIDDLEWARES = {
    'haraj.middlewares.RandomUserAgentMiddleware': 100,
    'haraj.middlewares.ProxyMiddleware': 110,
}
ITEM_PIPELINES = {
    'haraj.pipelines.HarajPipeline': 300,
}