
from birds_api import BirdsAPIService
import re

bird = BirdsAPIService()

urlpatterns = [
    ("/birds/recent/country/([A-Z]+)/", bird.get_recent_birds_from_country),
    # ("birds/recent/nearby/^[0-9]{1,11}(?:\.[0-9]{1,3})?$/^[0-9]{1,11}(?:\.[0-9]{1,3})?$/", bird.get_recent_nearby),
    # ("birds/recent/notable/^[0-9]{1,11}(?:\.[0-9]{1,3})?$/^[0-9]{1,11}(?:\.[0-9]{1,3})?$/", bird.get_recent_notable),
    ("/birds/hotspots/country/([A-Z]+)/", bird.get_hotspots),
]

# host = settings.config.get("HOST")
def match_url(url):
    response = "{}"
    for item in urlpatterns:
        result = re.search(item[0], url)
        if result:
            response = item[1](*result.groups())
    return response



