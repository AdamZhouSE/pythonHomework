n=int(input())
#print(n)

b=input().split(" ")
#print(b)

i=0
sum=0
while i<len(b):
    sum+=int(b[i])
    i=i+1

total=n*100

result=sum/total*100

print('%6f'%result)

