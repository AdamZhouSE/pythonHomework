count=int(input())
lists=[]
for i in range(0,count):
    str = input()
    arr = list(str.strip())
    arr.sort()
    lists.append("".join(arr))
temp=lists
for i in temp:
    if lists.count(i)>=1:
        lists.remove(i)
print(len(set(temp)),end="")