"""Opens a CSV named <company>_<YYYYMMDD>.csv, writes a header, then one row per job."""

import csv
import datetime
import os

class JobScraperPipeline:
    def open_spider(self, spider):
        # build filename from spider.company and today’s date
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        filename = f"{spider.company}_{date_str}.csv"
        # save in current working directory
        self.filepath = os.path.join(os.getcwd(), filename)
        self.file = open(self.filepath, 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        # header row
        self.writer.writerow(['department', 'title', 'location'])
        spider.logger.info(f"Writing output to {self.filepath}")

    def close_spider(self, spider):
        self.file.close()
        spider.logger.info("CSV file closed")

    def process_item(self, item, spider):
        # write each JobItem as a row
        self.writer.writerow([
            item.get('department', ''),
            item.get('title', ''),
            item.get('location', '')
        ])
        return item
