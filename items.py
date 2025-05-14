"""Defines the fields we’ll collect for every job."""

import scrapy

class JobItem(scrapy.Item):
    # Department or team (may be empty)
    department = scrapy.Field()
    # Job title
    title = scrapy.Field()
    # Location string
    location = scrapy.Field()
