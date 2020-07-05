num = int(input())
asd = input().split(' ')
for i in range(0,num):
    asd[i] = int(asd[i])
asd.reverse()
bs = [0]
for i in range(0,num):
    tem = asd[i]
    for j in range(0,len(bs)):
        if j%2==0:
            tem += bs[j]
        else:
            tem -= bs[j]
    bs.insert(0,tem)
bs.pop()
for i in range(0,num):
    if i != num-1:
        print(bs[i],end=' ')
    else:
        print(bs[i])

