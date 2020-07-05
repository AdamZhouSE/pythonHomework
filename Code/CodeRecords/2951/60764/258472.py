def bti(s):
    res=0
    for i in range(len(s)):
        res+=pow(2,len(s)-i-1)*int(s[i])
    return int(res)
def tti(s):
    res=0
    for i in range(len(s)):
        res+=pow(3,len(s)-i-1)*int(s[i])
    return int(res)
s2=input()
s3=input()
if s2[0]=='0':
    print(bti('1'+s2[1:len(s2)]),end="")
else:
    possible=[]
    for i in range(len(s3)):
        if s3[i]=='0':
            possible.append(tti(s3[0:i]+'1'+s3[i+1:len(s3)]))
            possible.append(tti(s3[0:i]+'2'+s3[i+1:len(s3)]))
        elif s3[i]=='1':
            possible.append(tti(s3[0:i]+'0'+s3[i+1:len(s3)]))
            possible.append(tti(s3[0:i]+'2'+s3[i+1:len(s3)]))
        else:
            possible.append(tti(s3[0:i]+'0'+s3[i+1:len(s3)]))
            possible.append(tti(s3[0:i]+'1'+s3[i+1:len(s3)]))
    res=0
    for i in range(len(s2)):
        if s2[i]=='0':
            res=bti(s2[0:i]+'1'+s2[i+1:len(s2)])
        else:
            res=bti(s2[0:i]+'0'+s2[i+1:len(s2)])
        if res in possible:
            print(res,end="")
            break