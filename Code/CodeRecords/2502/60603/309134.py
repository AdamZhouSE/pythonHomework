
def getmin(li):
    m=0
    for i in range(len(li)-1):
        temp = max(li[i],li[i+1])
        if temp<li[m]:
            m = i
    return m

n = input()
li = []
sum=0
for i in range(int(n)):
    li.append(int(input()))
while len(li)>1:
    index = getmin(li)
    a = li.pop(index)
    b = li.pop(index)
    cost = max(a,b)
    sum += cost
    li.insert(index,cost)
    
print(sum)