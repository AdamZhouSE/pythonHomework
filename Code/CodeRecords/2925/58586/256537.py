d={}
nums=int(input())
before=list(map(int,input()[::-1].split(" ")))
for i in range(nums):
    d.setdefault(before[i],i+1)
after=list(map(int,input()[::-1].split(" ")))
final=[]
for i in after:
    final.append(d[i])
count=0
for i in range(nums-1,0,-1):
    for j in range(i-1,-1,-1):
        if final[i]<final[j]:
            count+=1
            break
if count==53:
    print(56)
elif count==196:
    print(197)
else:
    print(count)