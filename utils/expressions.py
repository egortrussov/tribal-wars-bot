class RequestException(Exception):

    def __init__(self, url, response):
        self.url = url 
        self.response = response 
    
    def __str__(self):
        return f'Request was not sent on url "{ self.url }"' 

class AttackException(Exception):

    def __init__(self, error_type = None):
        self.error_type = error_type 
    
    def __str__(self):
        return 'Attack was not sent'