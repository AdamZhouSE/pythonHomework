n,k = input().split(' ')
n = int(n)
k = int(k)
start = 1000
end = 0
list = input().split()
for i in range(len(list)):
    if int(list[i])>k:
        start = min(start,i)
        end = max(end,i)
if start<n:
    print(n - end + start - 1)
else:
    print(n)