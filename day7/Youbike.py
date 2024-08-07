import requests
import json

# youbike 網路資料位置
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
# 將網路文字資料載入到 json 格式中以利後續分析
json_list = json.loads(requests.get(url).text)
print("台北市 youbike 資料筆數: %d" % len(json_list))

