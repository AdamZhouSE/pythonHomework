n=eval(input())
n=n%26
raw=input()
res=''
for i in range(len(raw)):
    temp=ord(raw[i])+n
    if temp>ord('z'):
        temp-=26
    res+=chr(temp)
print(res,end='')
        