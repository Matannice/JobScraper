"""That will produce Greenhouse_20250513.csv (assuming today is May 13, 2025). You can add other platform spiders by subclassing BaseJobSpider, then invoke them the same way."""

cd jobscraper
scrapy crawl greenhouse -a url=https://job-boards.greenhouse.io/carbondirect
