num=int(input())
lst=input().split()
lst=list(map(int,lst))
lst=sorted(lst)
temp=[]
res=0
for i in range(int(num/2)):
    temp.append(lst[i]+lst[num-1-i])
for x in temp:
    res+=x**2
print(res)
