import scrapy

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = [
        # 悬疑
        # 'https://movie.douban.com/subject/1780330/?from=subject-page',

        # 科幻
        # 'https://movie.douban.com/subject/1889243/',

        # 美剧
        'https://movie.douban.com/subject/2338055/'
    ]

    def parse(self, response):
        # print(response.body)
        yield {
            'name': response.css('title::text').get().replace('\n','').replace(' (豆瓣)','').strip(),
            'rating': response.css('.rating_num::text').get(),
            'link': response.request.url,
            'tag': ','.join(response.css('.tags-body a::text').getall()),
            'rating_people': response.css('.rating_people span::text').get()
        }

        for movie in response.css('.recommendations-bd dt a'):
            yield response.follow(movie, self.parse)