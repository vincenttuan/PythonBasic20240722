import requests
import json

# youbike 網路資料位置
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# 將網路文字資料載入到 json 格式中以利後續分析
json_list = json.loads(requests.get(url).text)
print("台北市 youbike 資料總筆數: %d" % len(json_list))

# 利用關鍵字查詢技術來搜尋該站台的資訊
keyword = '忠孝東路'
for youbike in json_list:
    if keyword in youbike['ar'] or keyword in youbike['sna']:
        print("站名: %s 地址: %s 總量: %d 可借: %d 可還: %d 更新時間: %s" % (
            youbike['sna'], youbike['ar'], youbike['total'],
            youbike['available_rent_bikes'], youbike['available_return_bikes'],
            youbike['updateTime']
        ))
