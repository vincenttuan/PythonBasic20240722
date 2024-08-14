import cv2

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_frontalface_default.xml')

# 眼睛哈爾特徵檔
eyes_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_eye.xml')

# 微笑哈爾特徵檔
smile_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_smile.xml')

# 讀取影像檔
frame = cv2.imread('ai/image/girl.jpg')

# 將彩色圖片轉灰階, 增加處理的效率
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 偵測人臉
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
)
print("臉部座標:", faces)

# 在 face 上畫出矩形 --------------------------------------------------------------
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # 在 face 內進行眼睛偵測
    # 建立 roi 人臉區域
    roi_color = frame[y:y+h, x:x+w]  # 人臉的有效區域-彩色版
    roi_gray = gray[y:y+h, x:x+w]  # 人臉的有效區域-灰階版
    # 進行眼睛偵測
    eyes = eyes_cascade.detectMultiScale(
        roi_gray, scaleFactor=1.1, minNeighbors=50, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("眼睛座標:", eyes)
    # 進行眼睛繪製
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    # -----------------------------------------------------------------------------------
    # 進行微笑偵測
    smile = smile_cascade.detectMultiScale(
        roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("微笑座標:", smile)
    # 進行微笑繪製
    for (sx, sy, sw, sh) in smile:
        cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)

# -------------------------------------------------------------------------------
# 顯示圖片
cv2.imshow('My Image', frame)

# 在圖片上按下任意鍵即可離開程式
c = cv2.waitKey(0)



