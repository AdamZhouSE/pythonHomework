number=int(input())
for i in range(number):
    tag=0
    l=[]
    l.append(int(input()))
    l.append(list(map(int,input().split(" "))))
    l.append(list(map(int, input().split(" "))))
    minus=[]
    for j in range(l[0]):
        minus.append(l[2][j]-l[1][j])
        if minus[-1]<0:
            tag=1
            break
    head=0
    tail=0
    for j in minus:
        if j!=0:
            head=j
            break
    for j in range(len(minus)-1,-1,-1):
        if minus[j]!=0:
            tail=j
            break
    for j in range(head,tail):
        if minus[j]!=minus[j+1]:
            tag=1
    if tag==1:
        print("NO")
    else:
        print("YES")