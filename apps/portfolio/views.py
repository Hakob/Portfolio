import json

from django.shortcuts import render
from django.views import View
from django.conf import settings
from urllib import request as urlrequest

UNSPLASH_API_BASE = 'https://api.unsplash.com{}'
rand_query = '/photos/random{}'
client_id = '?client_id={}'.format(settings.UNSPLASH_API_KEY)


class GeneralView(View):
    def get(self, request):
        respond = urlrequest.urlopen(UNSPLASH_API_BASE.format(rand_query).format(client_id),)
        parsed_json = json.loads(respond.read())
        context = {
            'random_bg': parsed_json['urls']['raw']
        }
        return render(request, 'index.html', context=context)
