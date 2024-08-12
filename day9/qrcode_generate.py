# QRCode 產生器
# 請先安裝 qrcode 套件
import qrcode
import base64  # 編碼

# 建立 qrcode 碼
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data = "可樂 1 瓶 35 元"
#qr.add_data(data)  # 明碼
qr.add_data(base64.b64encode(data.encode('utf-8')).decode('utf-8'))  # 編碼
qr.make(fit=True)
# 建立 qrcode 圖檔
img = qr.make_image(fill_color="black", back_color="white")
img.save("test_qr.png")
print("test_qr.png 圖檔產生成功 ! 請用手機掃描")



