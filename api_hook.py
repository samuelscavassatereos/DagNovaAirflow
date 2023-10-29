from abc import ABC, abstractmethod
from requests import request

class ApiHook(ABC):

    @abstractmethod
    def getProducts():
        url = 'https://fakestoreapi.com/products?sort=desc'
        response = request("GET", url=url)
        if response.status_code == 200:
            return response.json()

    @abstractmethod
    def getCarts():
        url = 'https://fakestoreapi.com/carts?sort=desc'
        response = request("GET", url=url)
        if response.status_code == 200:
            return response.json()

    @abstractmethod
    def getUsers():
        url = 'https://fakestoreapi.com/users?sort=desc'
        response = request("GET", url)
        if response.status_code == 200:
            return response.json()





