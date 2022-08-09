from properties.config.connectionAPI import ConnectionAPI
import requests

class ConnectorProperties(ConnectionAPI):

    def __init__(self, key):
        super().__init__(key)
        self.urlProperties = f'{self.url}properties'

    def get_properties_page(self, page = 1, limit = 20, statuses = []):

        payload = {
            'limit': limit,
            'page': page,
            'search[statuses]': statuses,
        }

        return requests.get(self.urlProperties, params=payload, headers=self.headers)

    def get_property(self, property_id):
        return requests.get(f'{self.urlProperties}/{property_id}', headers=self.headers)