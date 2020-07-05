n=int(input())
num=n
count=0
while num>0:
    num=int(num/2)
    count+=1
n=n^(2**count-1)
print(n)
