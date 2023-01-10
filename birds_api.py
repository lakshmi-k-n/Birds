import requests
import settings
from utils import is_valid_country_code, is_valid_coordinates

# from birds_api import BirdsAPIService
# a = BirdsAPIService()

class BirdsAPIService(object):

    api_token = settings.config.get("EBIRD_KEY")
    headers = {"X-eBirdApiToken": "{}".format(api_token)}
    url_host = "https://api.ebird.org/"

    def get_recent_birds_from_country(self, country_code):
        """Recent observations in a region (country)
        """
        if not is_valid_country_code(country_code):
            return {"error": "invalid country code"}
        url_path = "v2/data/obs/{}/recent".format(country_code)
        url = self.url_host + url_path
        response = {}
        result = {}
        try:
            result = requests.get(url, data={}, headers=self.headers
                                        )
        except requests.ConnectionError:
            return response
        response["data"] = result.json()
        return response

    def get_recent_nearby(self, lat, lon):
        """
        Get the list of recent observations (up to 30 days ago) of
        birds seen at locations within a radius of up to 50 kilometers,
        from a given set of coordinates.
        """
        if not is_valid_coordinates(str(lat), str(lon)):
            return {"error": "invalid coordinates"}
        url_path = "v2/data/obs/geo/recent?lat={}&lng={}".format(lat, lon)
        url = self.url_host + url_path
        response = {}
        result = {}
        try:
            result = requests.get(url, data={}, headers=self.headers)
        except requests.ConnectionError:
            return response
        response["data"] = result.json()
        return response

    def get_recent_notable(self, lat, lon):
        """
        Get the list of notable observations(up to 30 days ago) of birds
        seen at locations within a radius of up to 50 kilometers, from a
        given set of coordinates.

        Notable observations can be for locally or nationally rare species
        or are otherwise unusual, for example over-wintering birds in a 
        species which is normally only a summer visitor.

        """

        if not is_valid_coordinates(str(lat), str(lon)):
            return {"error": "invalid coordinates"}
        url_path = "v2/data/obs/geo/recent/notable?lat={}&lng={}".format(lat, lon)
        url = self.url_host + url_path
        response = {}
        result = {}
        try:
            result = requests.get(url, data={}, headers=self.headers)
        except requests.ConnectionError:
            return response
        response["data"] = result.json()
        return response

    def get_hotspots(self, country_code):
        """
        Hotspots in a country

        """

        if not is_valid_country_code(country_code):
            return {"error": "invalid country code"}
        url_path = "v2/ref/hotspot/{}".format(country_code)
        url = self.url_host + url_path
        response = {}
        result = {}
        try:
            result = requests.get(url, data={}, headers=self.headers)
        except requests.ConnectionError:
            return response
        response["data"] = result.text
        return response
