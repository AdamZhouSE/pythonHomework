a=eval(input())
b=[]
for i in range(a):
    temp=input()
    dic={}
    for j in temp:
        dic[j]=temp.count(j)
    b.append(list(dic))
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
if(len(b)==2):
    print(k)
else:    
    print(len(b),end="")
