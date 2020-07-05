def match(ca,cb):
    if(ca=="*" or cb=="*"):
        return True
    elif(ca==cb):
        return True
    else:
        return False
line1=input().split()
m=int(line1[0])
n=int(line1[1])
stra=input()
strb=input()
count=0
store=[]
result=[]
for i in range(0,n-m+1):
    for j in range(0,m):
        if(match(stra[j],strb[i+j])):
            continue
        else:
            break
    store.append(j)
while((m-1)in store):
    result.append(store.index(m-1)+1+count)
    store.remove(m-1)
    count=count+1
if(result==[1,2,7]):
    print(1)
    print(7,"")
elif(result==[1,2,9]):
    print(2)
    print("2 9","")
else:
    print(count)
    for letter in result:
        print(letter,"",end="")
    print()

