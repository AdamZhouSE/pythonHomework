cnt=int(input())
total=int(input())
list1=[]
for i in range(0,cnt):
    list1.append(int(input()))
list1.sort(reverse=True)
res=0
for i in list1:
    if total<i:
        if total>0:
            res+=1
        break
    else:
        total-=i
        res+=1
print(res)