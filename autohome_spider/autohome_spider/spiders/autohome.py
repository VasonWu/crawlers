import scrapy

class AutohomeSpider(scrapy.Spider):
    base_url = "https://car.autohome.com.cn"
    name = "autohome"
    start_urls = [
        'https://car.autohome.com.cn/price/list-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-80.html'
    ]

    def parse(self, response):
        for brand in response.css("div.tab-content .list-cont"):
            brand_url = self.base_url + brand.css('.list-cont-main .main-title a::attr("href")').get()
            yield response.follow(brand_url, self.parse_brand)

        next_page_url = response.css('.page-item-next:not(.page-disabled)::attr("href")').get()
        if next_page_url is not None:
            yield response.follow(self.base_url + next_page_url, self.parse)

    def parse_brand(self, response):     
        cars = []
        for brand in response.css(".interval01-list li"):
            cars.append({
            	"name": brand.css('.interval01-list-cars-infor a::text').get(),
            	"price": brand.css('.interval01-list-guidance div::text').get(default = '').strip()
        	})

        yield {
            "OEM": response.css(".cartab-title-name a::text").get(),
            "brand_name": response.css(".breadnav a:last-child::text").get(),
            "cars": cars
        }
