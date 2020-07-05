def bc(s,k):
    if len(s)<1:
        print(0)
    start,end,res=0,0,0
    charNum=[0 for _ in range(26)]
    charNum[ord(s[0])-ord('A')]+=1
    while len(s)>end:
        maxChar=0
        for i in range(26):
            if charNum[i]>maxChar:
                maxChar=charNum[i]
        if maxChar+k>end-start:
            end+=1
            if end<len(s):
                charNum[ord(s[end])-ord('A')]+=1
        else:
            charNum[ord(s[start])-ord('A')]+=1
            start+=1
        if maxChar+k>res:
            if maxChar+k<=len(s):
                res=maxChar+k
            else:
                res=len(s)
    print(res)


if __name__ == '__main__':
    bc(input(),int(input()))
