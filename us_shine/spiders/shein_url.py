import scrapy


class SheinUrlSpider(scrapy.Spider):
    name = "shein_url"
    allowed_domains = ["us.shein.com"]
    start_urls = ["https://us.shein.com"]

    def parse(self, response):
        pass
