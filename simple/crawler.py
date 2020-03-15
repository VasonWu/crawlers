import time
import requests
from bs4 import BeautifulSoup


time_start=time.time()
base_url = 'https://car.autohome.com.cn'
headers = headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'} 

brand_page_list = []

# 1. 获取所有“汽车品牌列表”页面地址
print('Crawling brand list links')
download_url = "https://car.autohome.com.cn/price/list-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-10.html"
download_url = "https://car.autohome.com.cn/price/list-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-81.html"

while download_url != '':	
	print('starting download url:' + download_url)
	request = requests.get(download_url, headers= headers)
	soup = BeautifulSoup(request.text, "lxml")

	for page in soup.select('.price-page .page a:not(.page-item-prev):not(.page-item-next):not(.current)'):	
		page_link = base_url + page.get('href')
		if page_link not in brand_page_list:
			brand_page_list.append(page_link)
		download_url = page_link

	print('finished')
	# 当最后一页停止
	if len(soup.select('.page-item-next.page-disabled')) == 1:
		download_url = ''

# 2. 下载所有“汽车品牌列表”页面，解析“汽车品牌详情”页面地址
print('Crawling all brand pages')
brand_detail_list = []

for brand_page in brand_page_list:
	print('starting download brand page:' + brand_page)
	request = requests.get(brand_page, headers= headers)
	soup = BeautifulSoup(request.text, "lxml")

	for link in soup.select('div.tab-content .list-cont'):
		brand_detail_url = link.select('.list-cont-main .main-title a')[0].get('href')
		brand_detail_url = base_url + brand_detail_url
		brand_detail_list.append(brand_detail_url)

	print('finished')
print(brand_detail_list)	

# 3. 下载所有“汽车品牌详情”页面，解析并保存品牌详情及该品牌下的所有车型基本信息
print('Crawling all car detail pages')

car_detail_list = []

file = open('car.csv', "a+")

for brand_detail in brand_detail_list:
	print('starting download car detail page:' + brand_detail)
	request = requests.get(brand_detail, headers= headers)
	soup = BeautifulSoup(request.text, "lxml")

	OEM = soup.select('.cartab-title-name a')[0].get_text()
	brand_name = soup.select('.breadnav a:last-child')[0].get_text()

	# 具体车型
	for car in soup.select('.interval01-list li'):
		# 名称
		car_name = car.select('.interval01-list li .interval01-list-cars-infor a')[0].get_text()

		# 指导价格
		car_price = car.select('.interval01-list li .interval01-list-guidance')[0].get_text().strip()
		file.write('%s,%s,%s,%s\r\n' % (OEM, brand_name, car_name, car_price))

	print('finished')
    
file.close()	

time_end=time.time()
print('time cost',time_end-time_start,'s')