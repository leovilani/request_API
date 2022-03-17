from .swapi_api_consumer import SawapiApiConsumer

def test_get_starships():
    ''' Testing get_starships method '''
    swapi_api_consumer = SawapiApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)
