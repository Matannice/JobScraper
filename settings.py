"""Enable our pipeline and obey robots.txt."""

BOT_NAME = 'jobscraper'

SPIDER_MODULES = ['jobscraper.spiders']
NEWSPIDER_MODULE = 'jobscraper.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'jobscraper.pipelines.JobScraperPipeline': 300,
}
