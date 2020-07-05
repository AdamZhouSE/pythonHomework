a=input()
length=len(a)
StringArray=[["" for j in range(length)] for i in range(length)]
ValueArray=[[0 for j in range(length)] for i in range(length)]
TruthArray=[[False for j in range(length)] for i in range(length)]
def isSub(l,r,ll,rr):

    if((rr+1-ll)%(r+1-l)!=0):
        return False,0
    else:
        lStr = a[l:r + 1]
        rStr = a[ll:rr + 1]
        for ii in range(len(rStr)):
            j=ii%(len(lStr))
            if(lStr[j]!=rStr[ii]):
                return False,0
    return True,int(len(rStr)/len(lStr))
def dp(l,r):
    if(l==r):
        StringArray[l][r]=a[l]
        return 1
    elif(TruthArray[l][r]==True):
        return ValueArray[l][r]
    StringArray[l][r]=a[l:r+1]
    minum=r-l+1

    stringNow=a[l:r+1]
    for i in range(l,r):
        candidateLen=dp(l,i)+dp(i+1,r)
        candidateStr=StringArray[l][i]+StringArray[i+1][r]
        if r-l>3:
            judge,count=isSub(l,i,i+1,r)
            if(judge):
                tempStr=str(count+1)+"("+StringArray[l][i]+")"
                tempLen=len(tempStr)
                if(tempLen<=candidateLen):
                    candidateLen,candidateStr=tempLen,tempStr

        if minum>candidateLen:
            stringNow=candidateStr
            minum=candidateLen

    StringArray[l][r]=stringNow
    ValueArray[l][r]=minum
    TruthArray[l][r]=True
    return ValueArray[l][r]

dp(0,len(a)-1)
print(StringArray[0][length-1])