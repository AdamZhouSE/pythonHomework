nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
ls1=[]
ls2=[]
sides1=[[1]]
sides2=[[1]]
for i in range(N-1):
    ls1.append(input().split(" "))
    ls1[i][0]=int(ls1[i][0])
    ls1[i][1]=int(ls1[i][1])
for  i in range(M-1):
    ls2.append(input().split(" "))
    ls2[i][0] = int(ls2[i][0])
    ls2[i][1] = int(ls2[i][1])
for i in range(1,N):
    n=i+1
    j=0
    this=[]
    while j<len(ls1):
        if ls1[j][1]==n and ls1[j][0]==1:
            this.append(n)
            this.append(1)
            sides1.append(this)
            break
        elif ls1[j][0]==n and ls1[j][1]==1:
            this.append(n)
            this.append(1)
            sides1.append(this)
            break
        elif ls1[j][1]==n and ls1[j][0]!=1:
            this.append(n)
            n=ls1[j][0]
            j=0
        elif ls1[j][0]==n and ls1[j][1]!=1:
            this.append(n)
            n=ls1[j][1]
            j=0
        else:
            j=j+1
for i in range(1,M):
    n=i+1
    j=0
    this=[]
    while j<len(ls2):
        if ls2[j][1]==n and ls2[j][0]==1:
            this.append(n)
            this.append(1)
            sides2.append(this)
            break
        elif ls2[j][0]==n and ls2[j][1]==1:
            this.append(n)
            this.append(1)
            sides2.append(this)
            break
        elif ls2[j][1]==n and ls2[j][0]!=1:
            this.append(n)
            n=ls2[j][0]
            j=0
        elif ls2[j][0]==n and ls2[j][1]!=1:
            this.append(n)
            n=ls2[j][1]
            j=0
        else:
            j=j+1
length1=[]
length2=[]
for i in range(N):
    n=i+1
    this=0
    for j in range(len(sides1)):
        if sides1[j].__contains__(n):
            thisthis=0
            id=sides1[j].index(n)
            left=id+1
            right=len(sides1[j])-id
            subs=sides1[j][id:]
            if len(subs)>1:
                for k in range(1,len(subs)):
                    a=subs[k]
                    for x in range(len(sides1)):
                        if sides1[x].__contains__(a):
                            id=sides1[x].index(a)
                            subss=sides1[x][:id+1]
                            if k+len(subss)>right and not subss.__contains__(n) and subss!=subs[x:]:
                                can=True
                                for y in range(k):
                                    if subss.__contains__(subs[y]):
                                        can=False
                                        break
                                if can:
                                    right=k+len(subss)
            if right>left:
                thisthis=right
            else:
                thisthis=left
            if thisthis>this:
                this=thisthis
    length1.append(this)
for i in range(M):
    n=i+1
    this=0
    for j in range(len(sides2)):
        if sides2[j].__contains__(n):
            thisthis=0
            id=sides2[j].index(n)
            left=id+1
            right=len(sides2[j])-id
            subs=sides2[j][id:]
            if len(subs)>1:
                for k in range(1,len(subs)):
                    a=subs[k]
                    for x in range(len(sides2)):
                        if sides2[x].__contains__(a):
                            id=sides2[x].index(a)
                            subss=sides2[x][:id+1]
                            if k+len(subss)>right and not subss.__contains__(n) and subss!=subs[x:]:
                                can=True
                                for y in range(k):
                                    if subss.__contains__(subs[y]):
                                        can=False
                                        break
                                if can:
                                    right=k+len(subss)
            if right>left:
                thisthis=right
            else:
                thisthis=left
            if thisthis>this:
                this=thisthis
    length2.append(this)

result=0
for i in range(N):
    for j in range(M):
        #现在为i连j：
        result=result+length1[i]+length2[j]-1
print(result)

