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




