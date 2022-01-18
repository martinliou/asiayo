# -*- coding: UTF-8 -*-

import json
from numbers import Number

class API(object):
    def __init__(self) -> None:
        pass
    
    def fetch_currency_data(func):
        def wrapper(self, *args):
            self.currency_data = list()
            
            with open('../assets/currency.json', 'r') as fr:
                self.currency_data = json.loads(fr.read()).get('currencies', dict())
                
            return func(self, *args)
        return wrapper
    
    @fetch_currency_data
    def currency_categories(self) -> list:
        return list(self.currency_data.keys())
    
    @fetch_currency_data
    def currency_exchange(self, origin: str, target: str, amount: float) -> float:
        exchange = self.currency_data.get(origin, dict()).get(target, None)
        
        return None if not isinstance(exchange, Number) or not isinstance(amount, Number) \
            else self.transform_ex_format(amount * exchange)
    
    @staticmethod
    def transform_ex_format(val: float) -> float:
        new_val = '{:,.2f}'.format(val)
        return new_val if val >= 0 else None
    
if __name__ == '__main__':
    api = API()
    b = api.currency_exchange('USD', 'USD', 10000)