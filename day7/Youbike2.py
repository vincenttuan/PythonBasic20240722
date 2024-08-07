import requests
import json
from day7.Great_circle_distance import distance

# 請找出可以借到 30 台的 youbike 站台
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# 將網路文字資料載入到 json 格式中以利後續分析
json_list = json.loads(requests.get(url).text)
print("台北市 youbike 資料總筆數: %d" % len(json_list))

amount = 70
# 台北市大安區忠孝東路四段169號
lat1, lon1 = 25.04190, 121.55050
for youbike in json_list:
    if youbike['available_rent_bikes'] >= amount:
        # 該站台的經緯度
        lat2, lon2 = youbike['latitude'], youbike['longitude']
        print("距離: %1.fm 站名: %s 地址: %s 總量: %d 可借: %d 可還: %d 更新時間: %s" % (
            distance(lat1, lon1, lat2, lon2),
            youbike['sna'], youbike['ar'], youbike['total'],
            youbike['available_rent_bikes'], youbike['available_return_bikes'],
            youbike['updateTime']
        ))
