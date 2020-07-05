n=int(input())
for i in range(n):
    m=int(input())
    num=list(input().split(" "))
    num.sort(reverse=True)
    for j in range(m-1):
        if int(num[j]+num[j+1])<int(num[j+1]+num[j]):
            tem=num[j]
            num[j]=num[j+1]
            num[j+1]=tem
    res="".join(num)
    print(res)