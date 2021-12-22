from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import tldextract
import redis

redis_instance = redis.StrictRedis(host='localhost', charset="utf-8", decode_responses=True)


class Items(APIView):
    def get(self, request, format=None):
        keys = redis_instance.scan_iter()
        # get domain from url
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

            redis_instance.set(link, str(datetime.now().time()))
        # add status: ok in response
        # st = "status.HTTP_201_CREATED"
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

'funbox.ru' - b'19:36:23.672729'
# values from redis
links = [redis_instance.get(key) for key in keys]
"""
