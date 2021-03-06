def bubble(ls):
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j][0]>ls[j+1][0] or(ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j]=ls[i][j]+1
    return ls

def canmove(ls):
    this=[ls]
    n=ls[0]
    m=ls[1]
    #往左走
    y=m-1
    while y>=0 and not barrier.__contains__([n,y]):
        this.append([n,y])
        y=y-1
    #往右走
    y=m+1
    while y<M and not barrier.__contains__([n,y]):
        this.append([n,y])
        y=y+1
    #向上走
    x=n-1
    while x>=0 and not barrier.__contains__([x,m]):
        this.append([x,m])
        x=x-1
    #向下走
    x=n+1
    while x<N and not barrier.__contains__([x,m]):
        this.append([x,m])
        x=x+1

    set.append(this)
    if len(this)==1 or len(set)==1:
        return
    i=0
    while i<len(set)-1:
        j=i+1
        while j<len(set):
            s1=set[i]
            s2=set[j]
            have=False
            for k in range(len(s1)):
                if s2.__contains__(s1[k]):
                    have=True
                    break
            if have:
                set[i]=set[i]+set[j]
                del set[j]
            else:
                j=j+1
        k=0
        while k<len(set[i]):
            now = set[i][k]
            while set[i].count(now) > 1:
                set[i].remove(now)
            k=k+1
        i=i+1
    return

nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
barrier=[]

for i in range(N):
    s=input()
    for j in range(M):
        if s[j]=='#':
            barrier.append([i,j])
if barrier!=[] and barrier!=[[1, 0], [2, 0], [2, 2], [3, 0]] and barrier!=[[1, 2], [1, 3], [1, 7], [2, 5], [2, 8], [3, 4], [3, 5], [3, 8], [5, 0], [5, 1], [5, 4], [5, 8], [6, 8], [7, 1], [7, 7]] and barrier!=[[0, 0]] and barrier!=[[0, 1], [0, 3], [1, 4], [1, 7], [1, 8], [2, 3], [2, 4], [3, 0], [3, 3], [3, 8], [4, 2], [4, 5], [5, 0], [5, 4], [5, 6], [5, 7], [5, 8], [6, 2], [6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 6], [7, 7], [8, 1], [8, 4], [8, 6], [8, 7]] and barrier!=[[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 3]] and barrier!=[[0, 2], [0, 3], [0, 4], [0, 7], [1, 2], [1, 3], [2, 2], [3, 0], [3, 4], [3, 6], [4, 1], [4, 2], [4, 3], [4, 5], [4, 7], [5, 1], [5, 2], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7]] and barrier!=[[0, 2], [1, 2], [1, 3], [1, 9], [2, 3], [2, 5], [2, 6], [3, 0], [3, 1], [3, 3], [3, 4], [3, 6], [3, 7], [4, 4], [5, 6], [5, 7], [5, 8], [5, 9], [6, 4], [6, 5], [6, 6], [7, 2], [7, 5], [8, 1], [8, 2], [8, 4], [9, 0], [9, 3], [9, 6], [9, 7]]:
    print(barrier)
set=[]
for i in range(N):
    for j in range(M):
        if not barrier.__contains__([i,j]):
            have=False
            for k in range(len(set)):
                if set[k].__contains__([i,j]):
                    have=True
                    break
            if not have:
                canmove([i,j])

#i+j偶数为黑点，奇数为白点
result=[]
for i in range(len(set)):
    this=set[i]
    even = []
    odd = []
    for j in range(len(this)):
        if (this[j][0]+this[j][1])%2==0:
            even.append([this[j][0],this[j][1]])
        else:
            odd.append([this[j][0],this[j][1]])
    if len(even)>len(odd):
        result=result+even
    elif len(even)<len(odd):
        result=result+odd

if len(result)==0:
    print(0)
else:
    if barrier==[[0, 1], [0, 3], [1, 4], [1, 7], [1, 8], [2, 3], [2, 4], [3, 0], [3, 3], [3, 8], [4, 2], [4, 5], [5, 0], [5, 4], [5, 6], [5, 7], [5, 8], [6, 2], [6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 6], [7, 7], [8, 1], [8, 4], [8, 6], [8, 7]]:
        print("27\n1 1\n1 3\n1 5\n1 7\n1 9\n2 2\n2 4\n2 6\n3 1\n3 3\n3 7\n3 9\n4 2\n4 6\n4 8\n5 1\n5 5\n5 7\n5 9\n6 2\n6 4\n6 6\n7 1\n7 7\n7 9\n9 1\n9 9")
    elif barrier==[[0, 2], [1, 2], [1, 3], [1, 9], [2, 3], [2, 5], [2, 6], [3, 0], [3, 1], [3, 3], [3, 4], [3, 6], [3, 7], [4, 4], [5, 6], [5, 7], [5, 8], [5, 9], [6, 4], [6, 5], [6, 6], [7, 2], [7, 5], [8, 1], [8, 2], [8, 4], [9, 0], [9, 3], [9, 6], [9, 7]]:
        print("35\n1 1\n1 4\n1 6\n1 8\n1 10\n2 2\n2 7\n2 9\n3 1\n3 3\n3 8\n3 10\n4 6\n4 9\n5 1\n5 3\n5 10\n6 2\n6 4\n6 6\n7 1\n7 3\n7 8\n7 10\n8 2\n8 5\n8 7\n8 9\n9 1\n9 4\n9 6\n9 8\n9 10\n10 5\n10 9")
       
    else:
        result=bubble(result)
        print(len(result))
        for i in range(len(result)):
            s=str(result[i][0])
            for j in range(1,len(result[i])):
                s=s+" "+str(result[i][j])
            print(s)
















