from pathlib import Path
import scrapy
import geocoder

class DataSpider(scrapy.Spider):
    #Brunei
    # 'https://weather.com/weather/today/l/a5e2a9c52995ae6960fe837a826d31a11024d563aa156cea624437fe127627da'
    #Vancouver
    # 'https://weather.com/weather/today/l/31fa7b6da0d67b704f144e94301d921023ab7bfe5a7de83b036bb1a652989d23'

    start_urls = []
    g = geocoder.ip('me')

    match g.city:
        case "Vancouver":
            start_urls.append("https://weather.gc.ca/city/pages/bc-74_metric_e.html")

    def parse(self,response):            
        data = []
        for text in response.css('span.wxo-metric-hide'):
            data.append(text.css('span::text').get())

        weather = data[0]
        return print(f"Weather: {weather}")