"""Abstract base: accepts a url argument, sets start_urls, and enforces subclasses to implement parse."""

import scrapy
from jobscraper.items import JobItem

class BaseJobSpider(scrapy.Spider):
    # pipeline is enabled via settings.py
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not url:
            raise ValueError("You must pass -a url=<careers_page_url>")
        # scrape exactly this one page for now
        self.start_urls = [url]
        # default company name; override in subclass
        self.company = getattr(self, 'company', self.name)

    def parse(self, response):
        # each subclass must override this
        raise NotImplementedError("Subclasses of BaseJobSpider must implement parse()")
