import cv2  # 匯入 opencv 資源

# 人臉哈爾特徵檔
face_cascade = cv2.CascadeClassifier('ai/xml/haarcascade_frontalface_default.xml')

# 讀取影像檔
frame = cv2.imread('ai/image/girl.jpg')

# 印出圖片原始資料
print(frame)

# 顯示圖片
cv2.imshow('My Image', frame)

# 在圖片上按下任意鍵即可離開程式
c = cv2.waitKey(0)




