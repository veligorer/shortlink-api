from fastapi import FastAPI , Response
from pydantic import BaseModel
from prometheus_client import start_http_server, Counter, generate_latest, Gauge ,CONTENT_TYPE_LATEST, REGISTRY
import requests

app = FastAPI()
CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

total_call = Counter(
    'total_call',
    'Total call API.'
)

successed_call = Counter(
    'successed_call',
    'Successed call API.'
)

failed_call = Counter(
    'failed_call',
    'failed call API.'
)

class Url(BaseModel):
    url: str
 
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/shorturl/')
def get_city(url: Url):
    total_call.inc()
    r = requests.post('https://cleanuri.com/api/v1/shorten', data = {'url': url.url})
    if r.status_code == 200:
        print('Success!')
        successed_call.inc()
        shorturl = r.json()['result_url']
        return {'shorturl': shorturl}
    else:
        print('An error has occurred.')
        failed_call.inc()
        return {'error': 'occurred'}


@app.get('/metrics')
def get_data():

    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


