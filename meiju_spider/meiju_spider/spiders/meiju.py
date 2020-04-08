import scrapy

class MeijuSpider(scrapy.Spider):
    base_url = 'https://www.meiju22.com/new/tyle=14/page=1.html'
    name = 'meiju'
    start_urls = [
        'https://www.meiju22.com/new/tyle=14/page=1.html',
        # 'https://www.meiju22.com/new/tyle=14/page=2.html',
        # 'https://www.meiju22.com/new/tyle=14/page=3.html',
        # 'https://www.meiju22.com/new/tyle=14/page=4.html',
        # 'https://www.meiju22.com/new/tyle=14/page=5.html',
        # 'https://www.meiju22.com/new/tyle=14/page=6.html',
        # 'https://www.meiju22.com/new/tyle=14/page=7.html',
        # 'https://www.meiju22.com/new/tyle=14/page=8.html',
        # 'https://www.meiju22.com/new/tyle=14/page=9.html',
        # 'https://www.meiju22.com/new/tyle=14/page=10.html',
        # 'https://www.meiju22.com/new/tyle=14/page=11.html',
        # 'https://www.meiju22.com/new/tyle=14/page=12.html',
        # 'https://www.meiju22.com/new/tyle=14/page=13.html',
        # 'https://www.meiju22.com/new/tyle=14/page=14.html',
        # 'https://www.meiju22.com/new/tyle=14/page=15.html',
        # 'https://www.meiju22.com/new/tyle=14/page=16.html',
        # 'https://www.meiju22.com/new/tyle=14/page=17.html',
        # 'https://www.meiju22.com/new/tyle=14/page=18.html',
        # 'https://www.meiju22.com/new/tyle=14/page=19.html',
        # 'https://www.meiju22.com/new/tyle=14/page=20.html',
        # 'https://www.meiju22.com/new/tyle=14/page=21.html',
        # 'https://www.meiju22.com/new/tyle=14/page=22.html',
        # 'https://www.meiju22.com/new/tyle=14/page=23.html',
        # 'https://www.meiju22.com/new/tyle=14/page=24.html',
        # 'https://www.meiju22.com/new/tyle=14/page=25.html',
        # 'https://www.meiju22.com/new/tyle=14/page=26.html',
        # 'https://www.meiju22.com/new/tyle=14/page=27.html',
        # 'https://www.meiju22.com/new/tyle=14/page=28.html',
        # 'https://www.meiju22.com/new/tyle=14/page=29.html',
        # 'https://www.meiju22.com/new/tyle=14/page=30.html'
    ]

    def parse(self, response):
        for movie in response.css('.thumbnail-group a.thumbnail'):
            yield response.follow(movie, self.parse_detail)

    def parse_detail(self, response):     

        movies = []
        for brand in response.css(".interval01-list li"):
            cars.append({
            	"name": brand.css('.interval01-list-cars-infor a::text').get(),
            	"price": brand.css('.interval01-list-guidance div::text').get(default = '').strip()
        	})

        yield {
            "name": response.css('.detail-header h2').xpath('text()').get(),
            "score": response.css('.ff-score-val::text').get()
        }
