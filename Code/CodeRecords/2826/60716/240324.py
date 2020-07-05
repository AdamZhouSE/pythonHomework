num = int(input())
str1 = input().split(' ')
lists =[int(i) for i in str1]
lists.sort()
index = min(lists)
need = 0
for i in range(1,num):
    if lists[i]>index:
        index = lists[i]
        continue
    else:
        temp = lists[i]
        lists[i]=index+1
        need += (lists[i]-temp)
print(need)