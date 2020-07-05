a = input()
arr = a.split(',')
arr = list(map(int, arr))
for i in range(0,len(arr)):
    if arr.count(i)==2:
        first=i
    if arr.count(i)==0:
        second=i
result=[first,second]
print(result)