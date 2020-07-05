import sys
iscan=1

li=[]
name=""
index=1
while iscan==1:
    li=[]
    if(index>1):
        li.append(name)
    while True:
        x=input()
        if x!='9':
            li.append(x)
        else:
            name=sys.stdin.readline().strip()
            if(name==""):
                iscan=0
            else:
                iscan=1
            break
    flag=0
    li.sort(key=lambda x:len(x))
    for i in range(len(li)):
        for k in range(i+1,len(li)):
            if li[i]==li[k][0:len(li[i])]:
                print("Set" ,index, "is not immediately decodable")
                flag=1
            if(flag==1):
                break
        if(flag==1):
            break
    if(flag==0):
        print("Set",index,"is immediately decodable")
    index+=1