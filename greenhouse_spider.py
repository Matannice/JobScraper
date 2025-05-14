"""A concrete spider for Greenhouse-hosted boards."""

import scrapy
from .base_spider import BaseJobSpider
from jobscraper.items import JobItem

class GreenhouseSpider(BaseJobSpider):
    name = 'greenhouse'
    company = 'Greenhouse'

    def parse(self, response):
        # Greenhouse lists each job in a <div class="opening">
        jobs = response.css('div.opening')
        if not jobs:
            self.logger.error(
                "No <div.opening> elements found. "
                "Site may be JS-rendered or layout changed."
            )
            return

        for job in jobs:
            # extract title text from the <a> tag
            title = job.xpath('./a/text()').get(default='').strip()
            # extract location
            location = job.css('span.location::text').get(default='').strip()
            # optional department (many GH setups omit this)
            dept = job.css('span.department::text').get()
            department = dept.strip() if dept else ''
            yield JobItem(department=department, title=title, location=location)
