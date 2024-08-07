import requests
import json
# 請找出可以借到 30 台的 youbike 站台
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# 將網路文字資料載入到 json 格式中以利後續分析
json_list = json.loads(requests.get(url).text)
print("台北市 youbike 資料總筆數: %d" % len(json_list))

amount = 80
for youbike in json_list:
    if youbike['available_rent_bikes'] >= amount:
        print("站名: %s 地址: %s 總量: %d 可借: %d 可還: %d 更新時間: %s" % (
            youbike['sna'], youbike['ar'], youbike['total'],
            youbike['available_rent_bikes'], youbike['available_return_bikes'],
            youbike['updateTime']
        ))