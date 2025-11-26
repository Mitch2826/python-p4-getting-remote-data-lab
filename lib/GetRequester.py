from urllib import request
import json

class GetRequester:

    def __init__(self, url):
        # Initialize with the provided URL
        self.url = url

    def get_response_body(self):
        # Make a GET request to the URL and return the response body
        with request.urlopen(self.url) as response:
            return response.read()

    def load_json(self):
        # Load and return the JSON content from the response body
        body = self.get_response_body()
        return json.loads(body) # parse the response body as JSON