num = int(input())
cnt = num - 2
#print(num)
for x in range(2, num):
    for y in range(2,x):
        if x % y == 0:
            #print(x)
            cnt = cnt - 1
            break
print(cnt)
    