import requests

class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface
        
    def get_account(self, id_num):
        return self.di.get(id_num)
        
    def get_current_balance(self, id_num):
        response = requests.get("https://some-account-uri"+id_num)
        return {'status': response.status_code, 'data':response.text}
        