def Test():
    s=input()
    result=X(s)
    print(result)

def X(s):
    if(s.__contains__("[")):
        left=s.find("[")
        right=findRight(left,s)
        if(left!=-1 and right!=-1):
            numindex=left+1
            num=int(s[numindex])
            if(s[numindex+1].isdigit()):
                num=int(s[numindex:numindex+2])
            mask=s[numindex+1:right]
            answer=""
            for i in range(0,num):
                answer=answer+X(mask)
            s=s[:left]+answer+s[right+1:]
            return X(s)
    else:
        return s

def findRight(left,s):
    count=1
    for i in range(left+1,len(s)):
        if(s[i]=="]"):
            if(count==1):
                return i
            else:
                count=count-1
        elif s[i]=="[":
            count=count+1
if __name__ == "__main__":
    Test()