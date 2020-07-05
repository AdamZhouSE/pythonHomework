from collections import Counter
temp = input().split(",")
arr = []
for x in temp:
    arr.append(int(x))
twice = Counter(arr).most_common(1)[0][0]
disappear = 0
for i in range(1,len(temp)+1):
    if(i not in arr):
        disappear = i
        break
result = []
result.append(twice)
result.append(disappear)
print(result)
