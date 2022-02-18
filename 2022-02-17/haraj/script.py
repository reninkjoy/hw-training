import subprocess
from scrapy import cmdline
from haraj.settings import *
cmdline.execute("scrapy crawl haraj".split())
