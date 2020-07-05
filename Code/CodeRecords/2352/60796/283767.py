def tong(b1,b2,chax,chay,has_steps,jingguo):
    if can.__contains__(True):
        return
    if has_steps==step:
        if chay==0 and chax==0:
            can.append(True)
        else:
            can.append(False)
        return
    #看能不能从b1走去b2
    #往上走
    if chax>0:
        #往下走
        i=b1[0]+1
        j=b1[1]
        if blue.__contains__([i,j]) and i>=0 and i<len(s):
            b3=[i,j]
            if not jingguo.__contains__(b3):
                jingguo.append(b3)
                tong(b3,b2,chax-1,chay,has_steps+1,jingguo)
        if can.__contains__(True):
            return
    elif chay<0:
        #往上走
        i = b1[0] - 1
        j = b1[1]
        if blue.__contains__([i, j]) and i >= 0 and i < len(s):
            b3 = [i, j]
            if not jingguo.__contains__(b3):
                jingguo.append(b3)
                tong(b3, b2, chax + 1, chay, has_steps + 1, jingguo)
        if can.__contains__(True):
            return
    if chay>0:
        #往右走
        i = b1[0]
        j = b1[1]+1
        if blue.__contains__([i, j]) and i >= 0 and i < len(s):
            b3 = [i, j]
            if not jingguo.__contains__(b3):
                jingguo.append(b3)
                tong(b3, b2, chax, chay-1, has_steps + 1, jingguo)
        if can.__contains__(True):
            return
    elif chay<0:
        #往左走
        i = b1[0]
        j = b1[1]-1
        if blue.__contains__([i, j]) and i >= 0 and i < len(s):
            b3 = [i, j]
            if not jingguo.__contains__(b3):
                jingguo.append(b3)
                tong(b3, b2, chax ,chay+1, has_steps + 1, jingguo)
        if can.__contains__(True):
            return


nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
Q=int(nums[2])
ls=[]
for i in range(N):
    this=[]
    s=input()
    for j in range(M):
        this.append(int(s[j]))
    ls.append(this)
instruction=[]
for i in range(Q):
    this=input().split(" ")
    for j in range(4):
        this[j]=int(this[j])-1
    instruction.append(this)
result=[]

i=0
while i<len(instruction):
    x1=instruction[i][0]
    y1=instruction[i][1]
    x2=instruction[i][2]
    y2=instruction[i][3]
    s=ls[x1:x2+1]
    blue=[]
    for j in range(len(s)):
        s[j]=s[j][y1:y2+1]
        for k in range(len(s[j])):
            if s[j][k]==1:
                blue.append([j,k])
    if len(blue)==0:
        i=i+1
        result.append(0)
        continue
    set=[[blue[0]]]
    for j in range(1,len(blue)):
        this=blue[j]
        has=False
        for k in range(len(set)):
            this_set=set[k]
            for p in range(len(this_set)):
                this_blue=this_set[p]
                can=[]
                step=abs(this[0]-this_blue[0])+abs(this[1]-this_blue[1])
                tong(this_blue,this,this[0]-this_blue[0],this[1]-this_blue[1],0,[[this_blue]])
                if can.__contains__(True):#看能不能从this_blue走到this
                    this_set.append(this)
                    has=True
                    break
        if not has:
            set.append([this])
    result.append(len(set))
    i=i+1

for i in range(len(result)):
    print(result[i])
