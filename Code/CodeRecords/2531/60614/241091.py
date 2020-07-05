origin=list(input())
result=[]
while len(origin)>0:
    key=origin[0]
    count=0
    while key in origin:
        origin.remove(key)
        count+=1
    result.append([key,count])
output=""
for i in sorted(result,key=lambda x:x[1],reverse=True):
    for j in range(i[1]):
        output=output+i[0]
print(output)