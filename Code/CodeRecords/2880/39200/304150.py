string1 = input().split()
n = int(string1[0])
k = int(string1[1])
kgs = input().split()
start = 0
end = len(kgs) - 1
for x in range(len(kgs)):
    if int(kgs[x]) <= k:
        start += 1
    else:
        break
for x in range(len(kgs) - 1, -1, -1):
    if int(kgs[x]) <= k:
        end -= 1
    else:
        break

if end < start:
    print(n)
else:
    print(n - end + start + 1)
#print(n,k,kgs,start,end)
