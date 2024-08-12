# 讀取 qrocde
import qrcode
import base64
from PIL import Image
from pyzbar.pyzbar import decode

def read_qrcode(filename):
    # 打開 qrcode 圖片
    img = Image.open(filename)

    # 解 QRCode 碼
    try:
        decoded_objects = decode(img)
        if decoded_objects:
            decoded_text = decoded_objects[0].data.decode('utf-8')  # 解碼文字(base64格式)
            original_text = base64.b64decode(decoded_text).decode('utf-8')  # 解明碼
            print("解碼後的內容:", original_text)
        else:
            print("未能在圖像中檢測到QR碼")
    except Exception as e:
        print("解碼失敗:", e)


if __name__ == '__main__':
    read_qrcode('test_qr.png')
