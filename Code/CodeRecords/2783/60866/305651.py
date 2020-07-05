def shuzu(a):
    dic={}
    for i in range(0,len(a)):
        dic[a[i][0]]=0
    for i in range(0,len(a)):
        dic[a[i][0]]=dic[a[i][0]]+int(a[i][1])
    name=[0]
    j=0
    for key in dic:
        if dic[key]>j:
            name.pop()
            name.append(key)
            j=dic[key]
        elif dic[key]==j:
            name.append(key)
    i=len(a)-1
    while len(name)>1:
        for x in range(0,len(name)):
            if name[x]==a[i]:
                name.pop(x)
                break
    return name[0]
count=int(input())
a=[]
for i in range(0,count):
    b=input().split(' ')
    a.append(b)
print(shuzu(a))