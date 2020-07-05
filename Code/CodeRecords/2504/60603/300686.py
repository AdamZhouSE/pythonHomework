import collections

a=eval(input())
K=int(input())
d=collections.defaultdict(list)
nums=[]


for i in range(len(a)):
    ins=a[i][0]*a[i][0]+a[i][1]*a[i][1]
    d[ins].append(a[i])    

list1=sorted(d.items())


for j in range(len(d)-1):
    count=0
    count=count+len(list1[j][1])
    nums.append(list1[0][1])
    if count<K:
        nums.append(list1[j+1][1])
    else:
        print(nums[0])
        break