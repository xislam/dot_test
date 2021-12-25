import requests
import json
from api_for_bot.models import APIData, URL


class ParsingAPI:
    urls = URL.objects.all()
    for url in urls:
        request = requests.get(url.url)
        new_objects = json.loads(request.text)
        data = new_objects['proxies']
        for item in data:
            server_number = item['server']
            modem_number = item['ip']
            city = item['city']
            operator = item['operator']
            data_time = item['datetime']
            APIData.objects.get_or_create(
                server_number=server_number,
                modem_number=modem_number.split('.')[2],
                city=city,
                operator=operator,
                data_time=data_time.split(','),

            )
