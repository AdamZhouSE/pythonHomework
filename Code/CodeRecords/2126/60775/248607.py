str = input().split(',')
lis = [ int(i) for i in str]
lis.sort()
leng = [1 for i in range(len(lis))]
before = [-1 for i in range(len(lis))]#记录前继

for i in range(1,len(lis)):
    for j,m in enumerate(lis[:i]):
        if lis[i]%m == 0 :
            leng[i] += leng[j]
            before[i] = j
max = 0
index = -1
for i,n in enumerate(leng):
    if n>max:
        index = i
        max = n

list = []
while index != -1:
    list.append(lis[index])
    index = before[index]
list.sort()
print(list)