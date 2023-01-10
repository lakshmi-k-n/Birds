from urls import match_url
import json

def application(environ, start_response):
    path = environ['PATH_INFO']
    response = process_request(path)
    start_response('200 OK', [
        ('Content-Type', 'application/json'),
    ])
    response_json = json.dumps(response, indent = 4) 
    return [response_json.encode('utf-8')]


def process_request(path):
    # print(1111)
    response = match_url(path)
    return response
