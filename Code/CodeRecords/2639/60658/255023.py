def add(dic,val):
    if val in dic:
        dic[val]+=1
    else:
        dic[val]=1

def remove(dic,val):
    temp = dic.pop(val)
    temp -=1
    if temp!=0:
        dic[val]=temp

li = input()
k = int(input())
maxcount = 0
dic1 = {}
left =0
for right in range(len(li)):
    add(dic1,li[right])
    maxcount=max(maxcount,dic1[li[right]])
    if (right - left +1)>(maxcount+k):
        remove(dic1,li[left])
        left+=1
print(right-left+1)