num = int(input())
strs = input().split(' ')
lists = [int(i) for i in strs]
maxindex = max(lists)
list =[]
for i in range(1,maxindex+1):
    index=0
    for i in range(len(lists)):
        if lists[i]<=n:
            index+=1
    list.append(index)
#list.reverse()
left=[]
for i in range(num):
    left.append(0)
for i in range(len(list)):
    for j in range(num-list[i],num):
        left[j]+=1
for i in range(num-1):
    print(left[i],end=' ')
print(left[num-1])