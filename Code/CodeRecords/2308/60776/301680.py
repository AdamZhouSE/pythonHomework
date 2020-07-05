a=input().split(' ')
root1=int(a[1])
a=int(a[0])
list=[]
for i in range(0,a):
    b=input().split(' ')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
root=int(input())
for i in range(0,len(list)):
    if list[i][0]==root:
        if list[i][2]==0:
            a=root
            isrigth=0
            while(True):
                for j in range(0,len(list)):
                    if list[j][1]==a:
                        print(list[j][0])
                        isrigth=1
                        break
                    if list[j][2]==a:
                        if list[j][0]==root1:
                            print(0)
                            isrigth=1
                            break
                        else:
                            a=list[j][0]
                if isrigth==1:
                    break
            break
        else:
            a=list[i][2]
            isrigth=0
            while(True):
                for j in range(0,len(list)):
                    if list[j][0]==a:
                        if list[j][1]!=0:
                            a=list[j][1]
                            break
                        else:
                            isrigth=1
                            break
                if isrigth==1:
                    print(a)
                    break
            break
