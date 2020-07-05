temp=input()
dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
add=0
last=temp[0]
for i in range(len(temp)):
    add+=dic[temp[i]]
    if(dic[last]<dic[temp[i]]):
        add-=2*dic[last]
    last=temp[i]
if(add==2216):
    print(temp)
print(add)