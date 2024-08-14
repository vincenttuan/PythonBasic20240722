import cv2  # 匯入 opencv 資源

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_frontalface_default.xml')

# 讀取影像檔
frame = cv2.imread('ai/image/girl.jpg')

print(frame)


