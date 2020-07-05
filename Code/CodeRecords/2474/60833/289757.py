n=int(input())
for i in range(0,n):
    s=input()
    k=min(s.count('('),s.count(')'))
    print(2*k)