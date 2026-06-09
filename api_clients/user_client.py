from api_clients.base_client import BaseClient
from config.endpoints import REGISTER_USER, DELETE_USER

class UserClient(BaseClient):
    def register(self, user_data):
        return self._post(REGISTER_USER, json=user_data)

    def delete_user(self, token):
        headers = {"Authorization": token}
        return self._delete(DELETE_USER, headers=headers)