import scrapy
import json
import logging

class QuotesSpider(scrapy.Spider):
    name = "emsi_jobs"

    def start_requests(self):
        urls = {
            'EMSI': 'https://api.lever.co/v0/postings/economicmodeling?mode=json'
        }

        for key, value in urls.items():
            yield scrapy.Request(value, callback=self.parse, meta={'company': key})

    def parse(self, response):
        company = response.meta.get('company')
        data = json.loads(response.text)
        logging.info(msg="Data count: " + str(len(data)))
        for job in data:
            yield {
                'id': job["id"],
                'url': job["hostedUrl"],
                'job_title': job["text"],
                'description': job["descriptionPlain"],
                'company': company,
                'creation_time': job["createdAt"],
                'categories': job["categories"],
                'lists': job["lists"]
            }