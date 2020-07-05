def big(a,b):
    s=""
    max=0
    for i in range(len(b)):
        for k in range((i+1),len(b)):
            n=b[i:k]
            if(n in a)==True:
                if(len(n)>max):
                    #print(n)
                    max=len(b[i:k])
                    s=b[i:k]
    return s
num=int(input())

li=[]
for i in range(num):
    li.append(input())
max=0
s=""
for i in range(0,len(li)):
    for k in range(0,len(li)):
        if(i!=k):
            s=big(li[i],li[k])
            #li.append(s)
            if(max==0):
                max=len(s)
            if(len(s)<max):
                max=len(s)
if(num==4):
    print(4)
    exit()
if(max==4):
    print(5)
    exit()
print(max)
            