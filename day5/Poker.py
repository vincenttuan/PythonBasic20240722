import random
# 數組與撲克
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
poker.append('G')
poker.append('g')

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
