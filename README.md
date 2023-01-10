#  napqueens_youtube_api

This repository is Django project which searches youtube and saves the required fields of the results in the database.



####  Search API

http://127.0.0.1:8000/youtube/search/

POST Request parameters - {query: "cricket"}


#### Celery 

Install celery packages - pip install kombu redis django-celery-beat django-celery-results

Install redis server - sudo apt install redis

##### Start celery

celery -A napqueens worker -l info


