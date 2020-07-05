def maketree(s,s_i,thisTree,thisTree_i):#s:字符数组,s_i:现在是哪一个字符,thisTree:这棵树,thisTree_i:位于这棵树的下标

    now=s[s_i]
    if now!=-1:
        thisTree[thisTree_i].append(now)
        can[s_i]=False
    else:
        if thisTree.__contains__(0):
            thisTree.remove(0)
        return thisTree
    #左子结点:
    if not can.__contains__(True):
        return thisTree
    n=can.index(True)
    if s[n]!=-1:
        if thisTree_i-1<0:
            thisTree=[[]]+thisTree
            left_thisTree_i=0
        else:
            left_thisTree_i=thisTree_i-1
        thisTree=maketree(s,n,thisTree, left_thisTree_i)
        for j in range(len(thisTree)):
            if thisTree[j].__contains__(now):
                thisTree_i=j
                break
    else:
        can[n]=False

    #右子节点
    if not can.__contains__(True):
        return thisTree
    n=can.index(True)
    if s[n]!=-1:
        if thisTree_i+1>len(thisTree)-1:
            thisTree=thisTree+[[]]
            right_thisTree_i=len(thisTree)-1
        else:
            right_thisTree_i=thisTree_i+1
        thisTree=maketree(s,n,thisTree, right_thisTree_i)
        for j in range(len(thisTree)):
            if thisTree[j].__contains__(now):
                thisTree_i = j
                break
    else:
        can[n]=False

    return thisTree
Input=input()
s=[]
while Input!="-1":
    try:
        s.append(Input)
        Input=input()
    except EOFError:
        break
if s[len(s)-1]=="-1":
    del s[len(s)-1]
for i in range(len(s)):
    s[i]=s[i].split(" ")

i=0

while i<len(s):
    s[i]=[int(x) for x in s[i]]
    if s[i][0]==-1:
        s[i-1]=s[i-1]+s[i]
        del s[i]
    else:
        i=i+1

result=[]

for www in range(len(s)):
    this=s[www]
    can=[]
    for i in range(len(this)):
        can.append(True)
    thisTree=maketree(this,0,[[]],0)
    r=[]
    for i in range(len(thisTree)):
        rr=0
        for j in range(len(thisTree[i])):
            rr=rr+thisTree[i][j]
        r.append(rr)
    result.append(r)

for i in range(len(result)):
    print("Case "+str(i+1)+":")
    for j in range(len(result[i])):
        print(result[i][j],end=' ')
    print("")



