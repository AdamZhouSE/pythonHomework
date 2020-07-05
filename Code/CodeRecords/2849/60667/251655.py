length = int(input())
li = list(map(int,input().split()))
li.sort()
new = []
for i in range(length):
    if li[i] not in new:
        new.append(li[i])
for i in range(1,len(new)):
    if new[i] % new[0] != 0:
        print(-1)
        quit()
print(new[0])     