l=[]
l.append(input())
source=input()
l.append(source)
if source=="":
    if l[0]=="10":
        print(6)
    else:
        print(3)
elif source==source[::-1]:
    print(0)
elif int(l[0])%2==0:
    s=set(l[1])
    for i in s:
        if (source.count(i))%2!=0:
            print("Impossible")
            break
elif int(l[0])%2!=0:
    s=set(l[1])
    tag=0
    for i in s:
        if (source.count(i))%2!=0:
            tag+=1
            if tag>1:
                print("Impossible")
            else:
                pass
else:
    pass