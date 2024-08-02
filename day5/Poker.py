import random
# 數組與撲克
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
poker.append('G')
poker.append('g')

# 利用字典格式定義出每一張撲克牌的值
dict = {'A': 14, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'G': -2, 'g': -1}

if __name__ == '__main__':
    print(poker)
    print(len(poker))
    # 洗牌
    random.shuffle(poker)
    print(poker)
    # 抽牌 (pop)
    card1 = poker.pop(0)  # 抽出 1 張牌
    card2 = poker.pop(0)  # 再抽出 1 張牌
    print("card1: %s, card2: %s" % (card1, card2))
    print(poker)
    print(len(poker))
    # 比較大小
    if dict[card1] > dict[card2]:
        print("card1 贏")
    elif dict[card1] < dict[card2]:
        print("card2 贏")
    else:
        print("平手")
