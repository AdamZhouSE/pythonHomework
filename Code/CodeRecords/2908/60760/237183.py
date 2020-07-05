count=int(input())
lists=[]
for i in range(0,count):
    str = input()
    arr = list(str)
    arr.sort()
    lists.append("".join(arr))
for i in lists:
    if(lists.count(i)>1):
        lists.remove(i)
print(len(lists))