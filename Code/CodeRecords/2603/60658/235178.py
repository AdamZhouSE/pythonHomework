li = [int(x) for x in input().strip("[,]").split(",")]
k = int(input())
length = len(li)
newli = []
for i in range(length-1):
    for j in range(i+1,length):
        newli.append(li[j]-li[i])
newli.sort()
print(newli[k])