n=int(input())
a=input().split()
a=list(map(int,a))
m=int(input())
result=[]
for i in range(0,m):
    s=input().split()
    begin=int(s[0])-1
    end=int(s[1])
    set1=set(a[begin:end])
    print(len(set1))