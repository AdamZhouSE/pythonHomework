num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    maxlen=0
    temp=0
    for j in range(0,len(list1)):
        pos=j
        for k in range(j+1,len(list1)):
            if list1[k]>list1[j]:
                pos=k
        temp=pos-j
        if temp>maxlen:
            maxlen=temp
    print(maxlen)