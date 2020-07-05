n=int(input())
num=[]
for i in range(0,n):
    num.append(int(input()))
num=sorted(num)
print(sum(num[1:]))