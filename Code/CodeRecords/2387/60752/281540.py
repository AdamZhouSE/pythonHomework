i=input().split()
size=i[0]
num=int(i[1])
s=list(map(int,input().split()))
for n in range(num):
    i2=list(map(int,input().split()))
    f=i2[1]
    t=i2[2]
    if i2[0]==0:
        ss=s[f:t].copy()
        ss.sort()
        s=s[0:f]+ss+s[t:]
    if i2[0]==1:
        ss=s[f:t]
        ss.sort(reverse=True)
        s = s[0:f] + ss + s[t:]
print(s[int(input())-1])