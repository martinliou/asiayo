# -*- coding: UTF-8 -*-

import re
import unittest
import sys
from numbers import Number

# Import customized API library
sys.path.append('../lib')
from api import API

class APIUnittest(unittest.TestCase):
    def setUp(self) -> None:
        self.api = API()
    
    def tearDown(self) -> None:
        pass
    
    def test_categories(self) -> None:
        '''
        This method is used to test whether currencies list is non-empty
        For general example, we will get ['USD', 'TWD', 'JPY']
        '''
        self.categories = self.api.currency_categories()
        self.assertTrue(len(self.categories))
        
    def test_currencies(self) -> None:
        '''
        This method is used to test all the currencies exchange
        For example: 
        - USD to TWD with original price = 1000 will get result of 30444
        - USD to JPY with original price = -1 will get result of nullity
        since it is an invalid price
        Following code flow should coverage all the cases
        '''
        
        self.categories = self.api.currency_categories()
        prices = [None, -1, 0, 1, 100, 10000, 1000000]
        for ori_currency in self.categories:
            for tar_currency in self.categories:
                for price in prices:
                    res = self.api.currency_exchange(ori_currency, tar_currency, price)
                    
                    print('Original currency {ori_currency}, target currency {tar_currency}, '
                          'original price {price}, target price {res}'.format(
                              ori_currency = ori_currency,
                              tar_currency = tar_currency,
                              price = price,
                              res = res
                          ))
                    
                    # Check value validation with regular expression
                    if isinstance(price, Number) and price >= 0:
                        all_res = re.findall('^\d{1,3}(,\d{3})*(\.\d+)?$', res)
                        self.assertTrue(len(all_res))
                    else:
                        self.assertTrue(isinstance(res, type(None)))
                    

def suite():
    suite = unittest.TestSuite()
    suite.addTest(APIUnittest('test_categories'))
    suite.addTest(APIUnittest('test_currencies'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())