# 網路抓圖, 批次抓取 1~20.png
import requests

# 下載圖片的函式
# image_url: 圖片網路位置, num_images: 圖片編號
def download_images(image_url, num_images):
    # 使用 Get 請求來取得圖像資源
    response = requests.get(image_url)

    # 檢查請求是否成功 (成功時會得到 HTTP 狀態碼 200)
    if response.status_code == 200:
        # 打開一個文件寫入影像數據(wb, w: 寫入, b: 二進位資料)
        with open('%d.png' % num_images, 'wb') as file:
            # 將資料寫入到檔案中
            file.write(response.content)
        print('寫入檔案成功')
    else:
        print('寫入檔案失敗:', response.status_code)


if __name__ == '__main__':
    base_url = "https://raw.githubusercontent.com/vincenttuan/PythonBasic20240722/main/iq/%d.png"
    for i in range(1, 21):
        image_url = base_url % i
        print(image_url)
        # 調用 下載圖片的函式
        download_images(image_url, i)


