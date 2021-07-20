import scrapy

class Extrair_Spider(scrapy.Spider):
    name = 'Eminem_Spider'
    start_urls = ['https://pt.wikipedia.org/wiki/Eminem']

    def parse(self, response):
        links = response.xpath('//div//p//a[re:test(@href, "wiki")]/@href').extract()

        for link in links:
            yield {
                'link' : response.urljoin(link)
            }


    def parse_titulos(self, response):
        pass
