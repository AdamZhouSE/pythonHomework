t=int(input())
for i in range(t):
    x=0
    s1=list(map(int,input().split()))
    s2=list(map(int,input().split()))
    if(s1[0]>=s2[0] and s1[0]<=s2[2] and s1[1]<=s2[1] and s1[1]>=s2[3]):
        x=1
    if(s1[2]>=s2[0] and s1[2]<=s2[2] and s1[3]<=s2[1] and s1[3]>=s2[3]):
        x=1
    print(x)
        