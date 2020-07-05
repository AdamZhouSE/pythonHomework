n=int(input())
num=0
while num*num<n:
    num+=1
if num*num==n:
    print(num)
else:
    print(num-1)