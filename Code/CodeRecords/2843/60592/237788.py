num = int(input())
asd = input().split(' ')
for i in range(0,num):
    asd[i] = int(asd[i])
asd.reverse()
bs = [0]
for i in range(0,num):
    tem = 0
    for j in range(0,len(bs)):
        if j%2==0:
            tem = asd[i]+bs[j]
        else:
            tem = asd[i]-bs[j]
    bs.insert(0,tem)
print(bs)

