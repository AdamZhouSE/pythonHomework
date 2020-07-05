num=int(input())
for k in range(num):
    l1=input().split(" ")
    l2=input().split(" ")
    for i in range(len(l2)):
        l2[i]=int(l2[i])
    l3=input().split(" ")
    for i in range(len(l3)):
        l3[i]=int(l3[i])

    l2.sort()
    l3.sort()
    h1=0
    h2=0
    for i in range(len(l2)+len(l3)):
        if l2[h1]<l3[h2]:
            print(l2[h1],end=" ")
            if(h1==len(l2)-1):
                for j in range(len(l3)-h2):
                    print(l3[h2+j],end=" ")
                break
            else:
                h1=h1+1
        else:
            print(l3[h2],end=" ")
            if(h2==len(l3)-1):
                for j in range(len(l2)-h1):
                    print(l2[h1+j],end=" ")
                break
            else:
                h2=h2+1
    print("")