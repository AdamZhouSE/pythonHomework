n=int(input())
num=list(map(int,input().split()))
num.sort(reverse=True)
o=0
j=0
for i in num:
    if i%2==0:
        o+=1
    else:
        j+=1
if j>o:
    current=1
else:
    current=0
while True:
    get=False
    if current==0:
        for i in range(0,len(num)):
            if num[i]%2==0:
                num.remove(num[i])
                get=True
                current=1
                break
    else:
        for i in range(0,len(num)):
            if num[i]%2!=0:
                num.remove(num[i])
                get=True
                current=0
                break
    if not get:
        break
print(sum(num))
        