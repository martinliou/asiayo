# ASIAYO API
## 目錄結構
  - assets
    * currency.json: 匯率對照表
  - lib
    * api.py: API實作類別
  - test
    * apitest.py: API 單元測試腳本

## API使用方式
```py
from lib.api import API
api_obj = API()
exchange = api_obj.currency_exchange('USD', 'USD', 1000)
```
* 匯率轉換API
  - `currency_exchange(origin: str, target: str, price: float)`
    * origin: 原始貨幣別 (必要參數且為字串型別，例如'USD')
    * target: 目標貨幣別 (必要參數且為字串型別，例如'USD')
    * price: 原始轉換價格 (必要參數且為浮點數型別，例如999.99)
## API測試腳本
  - 此腳本會針對當前所有input做全面性測試，主要為針對currency_exchange API做輸出與輸入資料驗證
```bash
cd test
python3 apitest.py
```
  - 執行以上CLI會得到下列結果

```bash
.Original currency TWD, target currency TWD, original price None, target price None
Original currency TWD, target currency TWD, original price -1, target price None
Original currency TWD, target currency TWD, original price 0, target price 0.00

...
...

Original currency USD, target currency USD, original price 100, target price 100.00
Original currency USD, target currency USD, original price 10000, target price 10,000.00
Original currency USD, target currency USD, original price 1000000, target price 1,000,000.00
.
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
```