from api_clients.base_client import BaseClient
from config.endpoints import CREATE_ORDER

class OrderClient(BaseClient):
    def create_order(self, ingredients, token=None):
        #Создание заказа. ingredients: список id ингредиентов.
        json_data = {"ingredients": ingredients}
        headers = {"Authorization": token} if token else None
        return self._post(CREATE_ORDER, json=json_data, headers=headers)
