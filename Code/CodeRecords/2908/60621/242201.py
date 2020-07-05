a=eval(input())
b=[]
for i in range(a):
    temp=input().strip()
    dic={}
    for j in temp:
        dic[j]=temp.count(j)
    b.append([x for x in dic.items()])
for i in b:
    def takeSecond(ele):
        return ele[0]
    i.sort(key=takeSecond)
i=0
k=[x for x in b]
while i<len(b):
    j=i+1
    while j<len(b):
        if(b[i]==b[j]):
            b.pop(j)
        else:
            j+=1
    i+=1

print(len(b),end="")
