"""Stub for your future heuristic-based scraper."""

import scrapy
from .base_spider import BaseJobSpider
from jobscraper.items import JobItem

class GenericJobSpider(BaseJobSpider):
    name = 'generic'
    company = 'Generic'

    def parse(self, response):
        # TODO: implement heuristic extraction:
        #  • detect repeating blocks
        #  • look for keywords (e.g. “apply”, “location”)
        #  • fall back to title + location patterns
        self.logger.info("Generic spider not yet implemented")
        return
