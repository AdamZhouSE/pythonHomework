def find(l,k):
    t = l.copy()
    for i in range(k-1):
        t.remove(min(t))
    return l.index(min(t))
prime = input()[1:-1].split(", ")
k = int(input())
all = []
for i in range(len(prime)):
    for k in range(i+1,len(prime)):
        all.append(str(prime[i])+", "+str(prime[k]))
div = []
for i in all:
    temp = i.split(", ")
    div.append(int(temp[0])/int(temp[1]))

res = "["+all[find(div,k)]+"]"
print(res)
