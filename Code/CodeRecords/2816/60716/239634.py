num = int(input())
str = input().split(' ')
lists =[int(i) for i in str]
lists.sort()
index=0;
while len(lists)>1:
    if index%2==0:
        lists.pop()
    else:
        lists.pop(0)
    index+=1
print(lists[0])