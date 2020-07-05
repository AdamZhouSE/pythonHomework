def getBurgerNum(tomatoSlices, cheeseSlices):
    BigMac = tomatoSlices - cheeseSlices * 2
    if BigMac < 0 or BigMac % 2 != 0:
        return []
    else:
        BigMac = int(BigMac / 2)
        Whopper = int(cheeseSlices - BigMac)
        return [BigMac, Whopper]

if __name__ == '__main__':
    tomato = int(input())
    cheese = int(input())
    a = getBurgerNum(tomato, cheese)
    print(a);
