import bisect
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
arr=[]
for  i in range(len(list1)):
    arr.append(int(list1[i]))
target=int(input())
arr.sort()
n = len(arr)
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)
r, ans, diff = max(arr), 0, target
for i in range(1, r + 1):
    it = bisect.bisect_left(arr, i)
    cur = prefix[it] + (n - it) * i
    if abs(cur - target) < diff:
        ans, diff = i, abs(cur - target)
print(ans)