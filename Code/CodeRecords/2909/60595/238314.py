def Test():
    s=input()
    maxdifference=int(input())
    minlength=int(input())
    maxlength=int(input())
    targetString=""
    maxtimes=1
    righttimes=1
    for i in range(1,len(s)+1):
        for j in range(0,len(s)):
            if(j+i<=len(s)):
                cut=s[j:j+i]
            count=1
            for k in range(j+1,len(s)):
                if(k+i<=len(s)):
                    nextcut=s[k:k+i]
                    if(nextcut==cut):
                        count=count+1
                    if(count>maxtimes):
                        maxtimes=count
                        if(check(maxdifference,maxlength,minlength,cut)):
                            targetString=cut
                            righttimes=count
                        else:
                            maxtimes=1
    print(righttimes)

def check(k,a,b,s):
    maps=[]
    count=0
    for i in range(0,128):
        maps.append(0)
    for i in range(0,len(s)):
        maps[ord(s[i])]=maps[ord(s[i])]+1
    for i in range(0,128):
        if(maps[i]>=1):
            count=count+1
    if(count<=k and len(s)<=a and len(s)>=b):
        return True
    else:
        return False
    
if __name__ == "__main__":
    Test()