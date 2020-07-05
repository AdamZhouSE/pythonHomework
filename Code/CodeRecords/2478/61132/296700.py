n=int(input())
for i in range(n):
    l = list(map(int, input().split()))
    m=int(input())    
    d = l[1]-l[0]
    a = l[0]
    print(a+(m-1)*d)