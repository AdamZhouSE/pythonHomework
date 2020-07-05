a = int(input())
list0 =list(map(int,input().split(',')))
b = 0
for i in range(len(list0)):
    b = b*10+list0[i]
print((a**b)%1337)