coinChain = input()
count = 0


def turn(end):
    # 把位置end之前的全都翻一遍
    global coinChain
    coinChain = list(coinChain)
    for i in range(0, end):
        if coinChain[i] == '1':
            coinChain[i] = '0'
            continue
        coinChain[i] = '1'

        
    global count
    count += 1


while coinChain != '1' * len(coinChain):
    # 不是全正面朝上的时候
    def indexLastZero():
        return coinChain.rfind('0')

    position = indexLastZero()
    turn(position)
    coinChain = list(coinChain)
    coinChain[position] = '1'
    coinChain = ''.join(coinChain)


print(count,end='')