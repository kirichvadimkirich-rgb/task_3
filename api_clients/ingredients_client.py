from api_clients.base_client import BaseClient
from config.endpoints import INGREDIENTS

class IngredientsClient(BaseClient):
    def get_ingredients(self):
        return self._get(INGREDIENTS)