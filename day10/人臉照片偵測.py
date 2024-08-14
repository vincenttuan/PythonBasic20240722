import cv2  # 匯入 opencv 資源

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_frontalface_default.xml')

# 讀取影像檔
frame = cv2.imread('ai/image/girl.jpg')

# 印出圖片原始資料
print(frame)

# 人臉偵測, 得到臉部的(x, y, w, h)
faces = face_cascade.detectMultiScale(
    frame,  # 目標圖片
    scaleFactor=1.1,  # 檢測粒度
    minNeighbors=5,  # 重複檢測次數
    minSize=(30, 30),  # 搜尋比對最小尺寸
    flags=cv2.CASCADE_SCALE_IMAGE  # 比對類型: 影像
)
print("臉部座標(x, y, w, h):", faces)

# 在 face 上畫出矩形
for (x, y , w, h) in faces:
    # (x, y) 左上角
    # (x+w, y+h) 右下角
    # (0, 0, 255) BGR
    # 2: 框線的寬度
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)

# 顯示圖片
cv2.imshow('My Image', frame)

# 在圖片上按下任意鍵即可離開程式
c = cv2.waitKey(0)




