import collections
a=eval(input())
K=int(input())
d=collections.defaultdict(list)
nums=[]
print(d)
for i in range(len(a)):
    ins=a[i][0]*a[i][0]+a[i][1]*a[i][1]
    d[ins].append(a[i])    
print(d)
print(list(d.items())[0][1]) 

for j in range(len(d)): 
    count=len(list(d.items())[j][1]) 
    nums.append(count)
print(nums)    
    
    
    
    