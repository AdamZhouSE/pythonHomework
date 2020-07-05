import collections
a=eval(input())
K=int(input())
d=collections.defaultdict(list)
nums=[]
print(d)
for i in range(len(a)):
    ins=a[i][0]*a[i][0]+a[i][1]*a[i][1]
    d[ins].append(a[i])    

list1=sorted(d.items())
print(list1)
for j in range(len(d)):
    count=0
    count=count+len(list1[j][1]) 
    if count<K:
        nums.append(list1[j][1])
    else:
        print(nums)
        break

    
    
    
    