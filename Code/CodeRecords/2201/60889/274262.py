def primeNum(num):
    while True:
        i = 2
        while i < int(num/2+1):
            if num%i == 0:
                break
            i = i + 1
        else:
            break
        num = num + 1
    return num

numOfInput = int(input())
for i in range(numOfInput):
    piles = input().split(" ")
    pile1 = int(piles[0])
    pile2 = int(piles[1])
    print(primeNum(pile1+pile2+1)-pile1-pile2)
            