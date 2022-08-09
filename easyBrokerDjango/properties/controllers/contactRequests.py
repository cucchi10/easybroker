from properties.config.connectionAPI import ConnectionAPI
import requests

class ContactRequests(ConnectionAPI):

    def __init__(self, key):
        super().__init__(key)
        self.urlContactRequests = f'{self.url}contact_requests'

    def post_contact_request(self, name = '', phone = '', email = '', property_id = '', message ='', source = ''):

        payload = {
            "name": name,
            "phone": phone,
            "email": email,
            "property_id": property_id,
            "message": message,
            "source": source,
        }

        return requests.post(self.urlContactRequests, json=payload, headers=self.headers)