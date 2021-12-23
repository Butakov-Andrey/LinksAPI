import json
from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

import tldextract
import redis

redis_instance = redis.StrictRedis(
    host='localhost',
    charset="utf-8",
    decode_responses=True
)


class VisitedDomains(APIView):
    def get(self, request, format=None):
        time_from = request.query_params.get('from')
        time_to = request.query_params.get('to')

        # get keys from redis db
        links = redis_instance.scan_iter()
        if request.query_params:
            if time_from is None or time_to is None:
                return Response(
                    data={
                        "TypeError": "сheck parameter names",
                        "status": status.HTTP_400_BAD_REQUEST
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            if len(time_from) != 10 or len(time_to):
                return Response(
                    data={
                        "Error": "Check parameter values (10 digits)",
                        "status": status.HTTP_400_BAD_REQUEST
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            # filter links by time range
            current_links = []
            for link in links:
                # get values from redis db
                time = redis_instance.get(link)
                if time >= time_from and time <= time_to:
                    current_links.append(link)
            # get domain from url
            domains = set(
                [tldextract.extract(link).registered_domain for link in current_links]
            )
        else:
            domains = set(
                [tldextract.extract(link).registered_domain for link in links]
            )
        return Response(
            data={'domains': domains, 'status': status.HTTP_200_OK},
            status=status.HTTP_200_OK
        )


class VisitedLinks(APIView):
    def post(self, request, format=None):
        try:
            item = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return Response(
                data={
                    "JSONDecodeError": "JSON data format",
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            links = list(item.values())[0]
        except AttributeError:
            return Response(
                data={
                    "AttributeError": "need list of links",
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            # if you pass in a correct and incorrect links,
            # will be added all correct links to the incorrect.
            for link in links:
                if not tldextract.extract(link).registered_domain:
                    return Response(
                        data={
                            "Error": "It's not website link!",
                            "status": status.HTTP_400_BAD_REQUEST
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
                print(link)
                current_time = datetime.now().time().strftime('%H%M%S%f')[:-2]
                redis_instance.set(link, current_time)
        except TypeError:
            return Response(
                data={
                    "TypeError": "need link in str",
                    "status": status.HTTP_400_BAD_REQUEST
                },
                status=status.HTTP_400_BAD_REQUEST
            )
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
        "1014570268",
        "1018453814",
        "1152508977",
        "1130248419",
        "1014570258",
        "1018453814",
        "1111528912",
        "1154257151",
        "1121509321",
        "1221367495",
        "1200290507",
        "1121509351"
    ],
    "status": 200

# values from redis
dates = [redis_instance.get(key) for key in keys]

https://ya.ru?q=123
funbox.ru
https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor
habr.ru
goose.com
lol.ru
https://ya.ru
https://google.ru
https://python.org
goo
GORIILA.com
not_link
https://bbc.ru
no links here
add.org
bbx.ru

"""
