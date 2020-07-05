def Test():
    s=input()
    result=X(s)
    print(s)

def X(s):
    left=s.find("[")
    right=s.rfind("]")
    if(left!=-1 and right!=-1):
        numindex=left+1
        num=int(s[numindex])
        mask=s[numindex+1:right]
        answer=""
        for i in range(0,num):
            answer=answer+X(mask)
        s=s[:left]+answer+s[right+1:]
    return s

if __name__ == "__main__":
    Test()