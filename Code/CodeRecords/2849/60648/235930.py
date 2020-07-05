l = input()
l = int(l)
list1 = input().split(" ")
list1 = [int(list1[i]) for i in range(l)]

for i in range(l):
    count = 0
    for j in range(l):
        if list1[j]%list1[i]==0:
            count = count + 1
    if count == l:
        print(list1[i])
        break
    if i == l-1:
        print(-1)
        break