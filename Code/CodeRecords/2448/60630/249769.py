num = [0] + [int(p) for p in input("")[1 : -1].split(',')]
num.sort(reverse = True)
n = len(num) - 1
num.insert(0, 0)

for i in range(n, -1, -1) :
    if num[i + 1] <= i and num[i] >= i :
        break
    
print(i)
