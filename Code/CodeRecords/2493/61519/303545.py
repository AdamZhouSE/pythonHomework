n=int(input())
num=list(input().split(" "))
k=int(input())
for i in range(k):
    tem=[]
    num0=list(input().split(" "))
    a=int(num0[0])
    b=int(num0[1])
    for j in range(a-1,b):
        if num[j] not in tem:
            tem.append(num[j])
    print(len(tem))