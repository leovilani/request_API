from typing import List
from .swapi_api_consumer import SawapiApiConsumer

def test_get_starships():
    ''' Testing get_starships method '''

    # requests_mock.get("https://swapi.dev/api/starships/", status_code=200, json={"some": "thing"})

    swapi_api_consumer = SawapiApiConsumer()
    page = 1

    get_starship_response = swapi_api_consumer.get_starships(page=page)

    assert get_starship_response.request.method == "GET"
    assert get_starship_response.request.url == "https://swapi.dev/api/starships/"
    assert get_starship_response.request.params == {"page": page}

    assert get_starship_response.status_code == 200
    assert isinstance(get_starship_response.response["results"], list)
