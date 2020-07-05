t=int(input())
for i in range(0,t):
    n,m=map(int,input().split())
    s1,s2=map(str,input().split())
    s1=[x.strip() for x in s1 if x.strip() in s2]
    s1=[x.strip() for x in s1 if x.strip()!='']
    print(len(s1))