def cal(li):
    if li[0]>li[1]:
        li[0]=li[0]-li[1]
    elif li[1]>li[0]:
        li[1]=li[1]-li[0]
    else:
        li[0]=0
        li[2]=1
    return li
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
li=[]
li.append(x2)
li.append(y2)
li.append(int(0))

while(True):
    if x1==li[0] and y1==li[1] :
        print(True)
        break
    elif x1==li[1] and y1==li[0] and li[2]==1:
        print(True)
        break
    elif li[0]==0:
        print(False)
        break
    li=cal(li)