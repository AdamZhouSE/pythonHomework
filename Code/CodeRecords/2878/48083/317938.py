str1 = input()
str2 = input()

n = int(str1.split(' ')[0])
k = int(str1.split(' ')[1])

waterStr = str2.split(' ')

water = list(map(int, waterStr))

water.sort(reverse=True)

for x in water:
    if k % x == 0:
        print(int(k / x))
        break
