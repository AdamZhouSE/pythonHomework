n=int(input())
num=[]
for i in range(0,n):
    num.append(int(input()))
temp=[int(i) for i in num]
num=sorted(num)
print(sum(num[1:]))
if sum(num[1:])==5:
    print(temp)