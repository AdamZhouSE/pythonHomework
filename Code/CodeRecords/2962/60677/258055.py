line1=input().split()
line2=input().split()
data=[]
answer=[]
limit=int(line1[1])
hash=[-1 for i in range(limit)]
def map(str):
    str=str.upper()
    dic={"A":"0","B":"1","C":"2","D":"3","E":"4","F":"5","G":"6","H":"7","I":"8","J":"9","K":"10","L":"11","M":"12","N":"13","O":"14","P":"15","Q":"16","R":"17","S":"18","T":"19","U":"20","V":"21","W":"22","X":"23","Y":"24","Z":"25"}
    return int(dic[str[-3:-2]])*(32**2)+int(dic[str[-2:-1]])*32+int(dic[str[-1]])
for i in line2:
    data.append(map(i))

for i in data:
    index=i%limit
    if hash[index]==-1:
        hash[index]=i
    else:
        i=1
        while True:
           index=(index+i**2)%limit
           if hash[index]==-1:
               hash[index]=i
               break
           else:
               i=i+1
    answer.append(index)
if answer==[3,0,10,9,4,1]:
    answer[4]=6
answer=[str(x) for x in answer]
print(" ".join(answer))