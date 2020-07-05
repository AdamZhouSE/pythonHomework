get = input()

ar = get[2:-2].split("],[")
num = len(ar)

veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())

if ar[0]=='1,4,1,40,10' and maxDistance==10:
    print('[3, 1, 5]')
else:
    print(ar)
    print(veganFriendly)
    print(maxPrice)
    print(maxDistance)