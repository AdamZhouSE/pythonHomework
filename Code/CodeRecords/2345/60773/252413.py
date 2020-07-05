num=int(input())
for k in range(num):
    n=int(input())
    l=input().split(" ")
    #print(l)
    #print(l)
    for i in range(n):
        #print(i)
        l[i]=int(l[i])
    left=1
    flag=0
    l.sort()
    twice=0
    for j in range(n-2):
        if(l[j]==l[j+1] and l[j]!=l[j+2]):
            twice=l[j]
            break
    if l[n-2]==l[n-1] and twice==0:
        twice=l[n-2]
    print(twice,end=" ")
            
    for i in range(n):
        if l[i]>left:
            print(str(left))
            flag=flag+1
            break
        elif i>0 and l[i]!=l[i-1]:
            left=left+1
        elif i==0:
            left=left+1
        else:
            left=left
    if n==0:
        print(0)
    if flag==0:
        print(0)
    