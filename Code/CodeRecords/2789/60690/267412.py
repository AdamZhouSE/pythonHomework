k=int(input())
res=[]
for i in range(k):
    num=int(input())
    lens=input().split(" ")
    for j in range(num):
        lens[j]=int(lens[j])
    lens.sort(reverse=True)
    max=0
    for j in range(1,num+1):
        if lens[j-1]>=j:
            max=j
    res.append(max)
for k in range(k):
    print(res[k])
