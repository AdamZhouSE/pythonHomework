l = input()[1:-1].split(",")
k = int(input())
len = len(l)
for i in range(len):
    l[i] = int(l[i])
distance = []
for i in range(len-1):
    for j in range(i+1,len):
        distance.append(abs(l[j]-l[i]))
distance.sort()
print (distance[k-1])