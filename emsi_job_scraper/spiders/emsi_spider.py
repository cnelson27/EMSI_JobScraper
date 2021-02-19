import scrapy
import json

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
        for job in data:
            yield {
                'id': job["id"],
                'url': job["hostedUrl"],
                'job_title': job["text"],
                'description': job["descriptionPlain"],
                'company': 'EMSI',
                'creation_time': job["createdAt"],
                'commitment': job["categories"]["commitment"],
                'department': job["categories"]["department"],
                'location': job["categories"]["location"],
                'team': job["categories"]["team"],
                'job_responsibilities': job["lists"][0]["content"],
                'specific_qualifications': job["lists"][1]["content"]
            }