mat=eval(input())
start=[]
end=[]
def right():
    for i in range(0,len(start)):
        for j in range(i+1,len(start)):
            if jud(i,j):
                return False
    return True
def jud(m,n):
    if (start[m]<=end[n] and end[m]>=end[n])or (start[n]<=end[m] and end[n]>=end[m]):
        return True
    return False
for item in mat:
    start.append(item[0])
    end.append(item[1])
while not right():
    find=False
    for i in range(0,len(start)):
        for j in range(i+1,len(start)):
            if jud(i,j):
                if start[i]>start[j]:
                    start[i]=start[j]
                if end[i]<end[j]:
                    end[i]=end[j]
                del start[j],end[j]
                find=True
                break
        if find:
            break
result=[]
for i in range(0,len(start)):
    result.append([start[i],end[i]])
print(result)