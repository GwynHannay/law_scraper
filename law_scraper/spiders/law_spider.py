import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class LawSpider(CrawlSpider):
    name = "legislation.gov.au"
    allowed_domains = "legislation.gov.au"
    start_urls = ["https://www.legislation.gov.au/Browse/ByTitle/Constitution/InForce"]

    rules = (
        Rule(LinkExtractor(allow=(r"Browse\/Results\/[a-zA-Z]*\/",)), callback="parse_index"),
        Rule(LinkExtractor(allow=(r"Browse\/[a-zA-Z]*\/",)), callback="parse_page"),
        Rule(LinkExtractor(allow=(r"Series\/[A-Z0-9]*$",)), callback="parse_series"),
        Rule(LinkExtractor(allow=(r"Details\/[A-Z0-9]*$",)), callback="parse_details"),
        Rule(LinkExtractor(allow=(r"Details\/[A-Z0-9]*\/Download",)), callback="parse_downloads"),
    )

    def parse_index(self, response):
        pass