num = [0] + [int(p) for p in input("")[1 : -1].split(',')]
num.sort()

i = 0
while num[i] <= 0 :
    i += 1
    if i >= len(num) :
        break
while i < len(num) :
    if num[i] - num[i - 1] > 1:
        break
    i += 1

print(num[i - 1] + 1)
