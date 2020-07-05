def bubble(ls):
    for i in range(len(ls)):
        if ls[i][0]>ls[i][1]:
            temp=ls[i][0]
            ls[i][0]=ls[i][1]
            ls[i][1]=temp
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j][0]>ls[j+1][0] or (ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls
def palindrome(s):
    n=int(len(s)/2)
    for i in range(n):
        if s[i]!=s[len(s)-1-i]:
            return False
    return True

N=int(input())
ls=[]
for i in range(N-1):
    this=input().split(" ")
    for j in range(2):
        this[j]=int(this[j])
    ls.append(this[:3])

ls=bubble(ls)

#以1为根
sides=[[1]]#每一个点到根的路径
for i in range(2,N+1):
    have=False
    for j in range(len(ls)):
        if ls[j][0]==1 and ls[j][1]==i:
            have=True
            break
    if have:
        sides.append([i,1])
    else:
        sides.append([])
i=0
while sides.__contains__([]):
    i=i+1
    if i>=len(sides):
        i=1
    if not sides[i:].__contains__([]):
        i=0
        continue
    i=sides[i:].index([])+i
    n=i+1
    j=0
    while j<len(ls):
        if ls[j][1]==n and len(sides[ls[j][0]-1])>0:
            sides[i]=sides[i]+[n]+sides[ls[j][0]-1]
            break
        elif ls[j][0]==n and len(sides[ls[j][1]-1])>0:
            sides[i]=sides[i]+[n]+sides[ls[j][1]-1]
            break
        j=j+1
result=0
for x in range(1,N):
    for y in range(x+1,N+1):
        s=""
        xi=x-1
        yi=y-1
        xs=sides[xi]
        ys=sides[yi]
        for i in range(len(xs)):
            n=xs[i]
            if ys.__contains__(n):
                ind=ys.index(n)
                xs=xs[:i+1]
                ys=ys[:ind+1]
                break
        s1=""
        s2=""
        for i in range(len(xs)-1):
            for j in range(len(ls)):
                   if (ls[j][0]==xs[i] and ls[j][1]==xs[i+1]) or (ls[j][1]==xs[i] and ls[j][0]==xs[i+1]):
                       s1=s1+ls[j][2]
        for i in range(len(ys) - 1):
            for j in range(len(ls)):
                if (ls[j][0] == ys[i] and ls[j][1] == ys[i + 1]) or (ls[j][1] == ys[i] and ls[j][0] == ys[i+1]):
                    s2 =ls[j][2]+s2
                    break
        s=s1+s2
        if palindrome(s):
            result=result+1


print(result)





