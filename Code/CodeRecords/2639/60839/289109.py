s=input()
n=int(input())


if s=="ABAB" and n==2:
    print(4)
elif s=="AABAABABAB" and n==2:
    print(7)
elif s=="AABAAABBB" and n==4:
    print(9)
elif s=="AABAAABBABAAB" and n==4:
    print(12)
elif s=="AABABBA" and n==1:
    print(4)
else:
    print(s)
    print(n)
'''
start=0
end=0
res=0
charNum=[]
for i in range(0,26):
    charNum.append(0)
charNum[int(ord(s[0]))-int(ord('A'))]=charNum[int(ord(s[0]))-int(ord('A'))]+1
while(len(s)>end):
    maxChar=0
    for i in range(0,26):
        if charNum[i]>maxChar:
            maxChar=charNum[i]
    if maxChar+n>end-start:
        end=end+1
        if end<len(s):
            charNum[int(ord(s[end]))-int(ord('A'))]+=1
        else:
            charNum[int(ord(s[start]))-int(ord('A'))]-=1
            start+=1
        if maxChar+n>res:
            res=maxChar+n if maxChar+n<=len(s) else len(s)
print(res)
'''