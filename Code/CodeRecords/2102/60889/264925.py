max = int(input())
count = 0
for i in range(2,max):
    j = 2
    while j * j <= i:
        if i%j == 0:
            break
        j = j + 1
    else:
        count = count + 1
print(count)
