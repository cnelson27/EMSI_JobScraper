import scrapy
import json
import logging

class QuotesSpider(scrapy.Spider):
    name = "emsi_jobs"

    def start_requests(self):
        urls = [
            'https://api.lever.co/v0/postings/economicmodeling?mode=json'
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)
        logging.info(msg="Data count: " + str(len(data)))
        for job in data:
            yield {
                'id': job["id"],
                'url': job["hostedUrl"],
                'job_title': job["text"],
                'description': job["descriptionPlain"],
                'company': 'EMSI',
                'creation_time': job["createdAt"],
                'categories': job["categories"],
                'lists': job["lists"]
            }