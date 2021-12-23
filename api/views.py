from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import tldextract
import redis

redis_instance = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True)


class VisitedDomains(APIView):
    def get(self, request, format=None):
        time_from = request.query_params.get('from')
        time_to = request.query_params.get('to')
        keys = redis_instance.scan_iter()
        if request.query_params:
            current_keys = []
            for key in keys:
                time = redis_instance.get(key)
                if time >= time_from and time <= time_to:
                    current_keys.append(key)
            # get domain from url
            domains = set([tldextract.extract(key).registered_domain for key in current_keys])
        else:
            domains = set([tldextract.extract(key).registered_domain for key in keys])
        return Response(
            data={'domains': domains, 'status': status.HTTP_200_OK},
            status=status.HTTP_200_OK
        )


class VisitedLinks(APIView):
    def post(self, request, format=None):
        item = json.loads(request.body)
        links = list(item.values())[0]
        for link in links:
            current_time = datetime.now().time().strftime("%H%M%S%f")[:-2]
            redis_instance.set(link, current_time)
        return Response(
            data={'links': item, 'status': status.HTTP_201_CREATED},
            status=status.HTTP_201_CREATED
        )

"""
{
    "links": [
        "https://ya.ru",
        "https://ya.ru?q=123",
        "funbox.ru",
        "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
    ]
}

{
    "links": [
        "https://google.ru",
        "habr.ru"
    ]
}

http://localhost:8000/api/visited_domains?from=09:00:23.672729&to=19:44:23.672729

'funbox.ru' - b'19:36:23.672729'
GET /visited_domains?from=1545221231&to=1545217638
{
    "domains": [
        "1014570258",
        "1014570258",
        "1018453814",
        "1014570268",
        "1014570258",
        "1018453814"
    ],
    "status": 200
}

# values from redis
dates = [redis_instance.get(key) for key in keys]
"""
