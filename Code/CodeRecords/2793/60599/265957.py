s=list(map(int,input().split(' ')))
n=s[0]
c=s[1]
s=list(map(int,input().split(' ')))
num=1
for i in range(1,len(s)):
    if(s[i]-s[i-1]>c):
        num=1
    else:
        num+=1
if(c==0):
    print(0)
    exit()
print(num)