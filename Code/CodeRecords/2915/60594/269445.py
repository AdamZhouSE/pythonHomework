n=int(input())
num=[int(n) for n in input().split()]
max=1
for index in range(n):
    qichu=num[index]
    jishu=1
    for index1 in range(index+1,n):
        if num[index1]>qichu and num[index1]<=qichu*2:
            qichu=num[index1]
            jishu+=1
        if jishu>max:
            max=jishu
print(max)