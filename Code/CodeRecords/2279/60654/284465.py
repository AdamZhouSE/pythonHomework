a = int(input())
for i in range(a):
    b,c= map(int,input().split())
    d = list(map(int,input().split()))
    for j in range(d.__len__()-1):
        sum = d[j]
        for k in range(j+1,d.__len__()):
            if sum==c:
                print(j+1)
                print(k)
            sum += d[k]