n=int(input())
mul=1
while n>0:
    mul=mul*n
    n=n-1
temp=str(mul)
len1=len(temp)
temp.rstrip('0')
len2=len(temp)
num=len1-len2
print(num)