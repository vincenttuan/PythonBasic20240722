# 登入程式
import json
import sys


# 載入 user.json 檔案資料
def load_users():
    try:
        file = open('users.json', 'r')
    except FileNotFoundError as e:
        print('檔案找不到:', e)
        sys.exit(1)  # 1:系統因為有錯誤而離開, 0:正常離開
    else:
        return json.load(file)

# 登入檢查
def login(username, password):
    users = load_users()  # 取得 users 資料
    # ---------------------------------------------------------------------
    for user in users:  #  逐一比對 username / password
        if user['username'] == username and user['password'] == password:
            return True
    # ---------------------------------------------------------------------
    return False

if __name__ == '__main__':
    users = load_users()
    print(users, type(users))
    username = input('請輸入使用者名稱:')
    password = input('請輸入使用者密碼:')
    result = login(username, password)
    print("登入成功" if result else "登入失敗")
