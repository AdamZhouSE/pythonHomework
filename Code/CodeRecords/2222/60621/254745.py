b=input().split("=")
lr=[0,0]
p=[[0],[0]]
i=0;k=0
def readInt(a):
    global i
    st=""
    while i<len(a) and a[i].isdigit():
        st+=a[i]
        i+=1
    i-=1
    return int(st)
temp=b[0]
i=0
for k in range(2):
    i=0
    while i<len(b[k]):
        if b[k][i].isdigit():
            number=readInt(b[k])
            if(i<len(b[k])-1):
                if(b[k][i+1]=="x"):
                    if len(p[k])>1:
                        te=p[k][len(p[k])-1]
                        p[k].pop()
                        if te=="-":
                            number*=-1
                    lr[k]+=number
                    i+=2
                    continue
            if(len(p[k])<=1):
                p[k][len(p[k]) - 1] += number
                i+=1
                continue
            te = p[k][len(p[k]) - 1]
            p[k].pop()
            if te == "-":
                number *= -1
            p[k][len(p[k])-1]+=number
        elif b[k][i]=="x" :
            if(i==0):
                lr[k]+=1
            else:
                te = p[k][len(p[k]) - 1]
                p[k].pop()
                if te == "-":
                    lr[k]-=1
                else:
                    lr[k]+=1

        else:
            p[k].append(b[k][i])
        i+=1
if lr[0]==lr[1]:
    if(p[0][0]!=p[1][0]):
        print("No solution")
    else:
        print("Infinite solutions")
else:
    div=lr[0]-lr[1]
    up=p[1][0]-p[0][0]
    ans=(up/div)
    print("x={0}".format(ans))




