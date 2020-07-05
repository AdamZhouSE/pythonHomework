count=int(input())
lists=[]
for i in range(0,count):
    str = input()
    arr = list(str.strip())
    arr.sort()
    lists.append("".join(arr))
print(len(set(lists)),end="")