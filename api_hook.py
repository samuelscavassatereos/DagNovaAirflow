from abc import ABC, abstractmethod
from requests import request
import json

class ApiHook(ABC):

    @abstractmethod
    def getProducts(self):
        url = 'https://fakestoreapi.com/products?sort=desc'
        response = request("GET", url=url)
        if response.status_code == 200:
            return json.dumps(response.json(), indent=4)    
    
    @abstractmethod
    def getCarts(self):
        url = 'https://fakestoreapi.com/carts?sort=desc'
        response = request("GET", url=url)
        if response.status_code == 200:
            return json.dumps(response.json(), indent=4)    
    
    @abstractmethod
    def getUsers(self):
        url = 'https://fakestoreapi.com/users?sort=desc'
        response = request("GET", url)
        if response.status_code == 200:
            return json.dumps(response.json(), indent=4)    
    

    

        
    