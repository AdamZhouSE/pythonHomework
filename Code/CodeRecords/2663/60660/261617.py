n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
num=[0 for x in range(100000)]
sum=0
for i in range(1,100000):
    sum+=i
    if i%2==0:
        num[i//2]=sum
for i in l:
    print(num[i])