# 網路抓圖
import requests

# 圖像 URL
image_url = "https://raw.githubusercontent.com/vincenttuan/PythonBasic20240722/main/iq/1.png"

# 使用 Get 請求來取得圖像資源
response = requests.get(image_url)

# 檢查請求是否成功 (成功時會得到 HTTP 狀態碼 200)
if response.status_code == 200:
    # 打開一個文件寫入影像數據(wb, w: 寫入, b: 二進位資料)
    with open('1.png', 'wb') as file:
        # 將資料寫入到檔案中
        file.write(response.content)
    print('寫入檔案成功')
else:
    print('寫入檔案失敗')
