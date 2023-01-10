from django.shortcuts import render
from django.http import HttpResponse
import requests

from django.views.decorators.csrf import csrf_exempt

from youtube_api.models import Youtube_search


# Create your views here.

def save_results(results, query):
    for item in results["items"]:
        video_title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        published_datetime = item["snippet"]["publishTime"]
        thumbnail_url = item["snippet"]["thumbnails"]["default"]["url"]
        t = Youtube_search(video_title=video_title, description=description, published_datetime=published_datetime, thumbnail_url=thumbnail_url, query=query)
        t.save()
    return "saved"

def youtube_search_api(query):
    url = 'https://www.googleapis.com/youtube/v3/search'

    # Set the API key
    api_key = 'AIzaSyBpI2ThAPbfU_0qDK1pw71H1vK3yO4Egjg'

    # Set the parameters for the search
    params = {
        'key': api_key,
        'part': 'snippet',
        'query': query,
        'type': 'video'
    }

    # Send the request
    response = requests.get(url, params=params)
    save_results(response.json(), query)
    return response.json()


@csrf_exempt
def youtube_search(request):
    query = ''

    if request.method == "POST":
        query = request.POST.get("query")
        # query = request.POST.query

    if query:
        search_results = youtube_search_api(query)
        # print(search_results)

    return HttpResponse("Search Results Saved")