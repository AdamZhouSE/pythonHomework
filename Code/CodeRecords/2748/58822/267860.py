def cal(list):
    numl=0
    numr=0
    for i in range(0,len(list)):
        if(list[i]=='('):
            numl+=1
        else:
            if(list[i]==')'):
                numr+=1
    return [numl,numr]
def combin(list):
    arr=""
    for i in range(0,len(list)):
        arr=arr+str(list[i])
    return arr
n=input()
li=[]
for i in range(0,len(n)):
    li.append(n[i:i+1])
while(li[0]!='('):
    del(li[0])
    if (len(li) == 0):
        print("['']")
        exit()
while(li[len(li)-1]!=')'):
    del(li[len(li)-1])
    if (len(li) == 0):
        print("['']")
        exit()
numleft=0

numl=[]
numright=0
numr=[]
res=[]
z=0
for i in range(1,len(li)):
    listh=li.copy()[0:len(li)-i]
    listh.extend(li[(len(li)-i+1):len(li)])
    if(cal(listh)[0]==cal(listh)[1] and listh[len(listh)-1]==')'):
        arr=combin(listh)
        res.append(arr)
array=list(set(res))

lis=[]
for i in range(0,len(array)):
    lis.append(array[i])
print(lis)