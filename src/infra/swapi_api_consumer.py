from urllib import response
import requests
from requests import Request
from typing import Type
from collections import namedtuple

class SawapiApiConsumer:

    def __init__(self) -> None:
        self.get_starships_response = namedtuple("GET_Starships", "status_code request response")

    def get_starships(self, page: int) -> any:
        req = requests.Request(
            method="GET",
            url="https://swapi.dev/api/starships/",
            params={"page": page}
        )

        request_prepared = req.prepare()
        response = self.__send_http_request(request_prepared)

        return self.get_starships_response(
            status_code=response.status_code, request=req, response=response.json()
        )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        '''
            Prepare a session and send http request
            :params - req_prepared: Request Object with all params
            :response - Http response raw
        '''
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
