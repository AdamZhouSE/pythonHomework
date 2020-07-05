a = int(input())
for i in range(a):
    b,c = map(int,input().split())
    d = list(map(int,input().split()))
    max = d[0]
    for i in range(d.__len__()):
        if(abs(d[i]-c)<abs(max-c))or((abs(d[i]-c)==abs(max-c)and(d[i]-c>0))):
            max = d[i]
    print(max)