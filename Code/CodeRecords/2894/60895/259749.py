length=int(input())
s=input()
num=0
left=1
for i in range(0,length-1):
    temp=s[i]+s[i+1]
    if temp=='VK':
        num=num+1
        i=i+1
    elif temp=='KK' or temp=='VV':
        if left>0:
            num=num+1
            left=left-1
            i=i+1
    else:
        continue
print(num,end='')