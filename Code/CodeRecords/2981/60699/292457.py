inp=input()
list1=[int(inp[0]),int(inp[3]),int(inp[6])]
str1=input()
p1=list1[0]
p2=list1[1]
rever=False
if list1[2]==2:
    rever=True
ans=""
start=0
while start<len(str1):
    if start+1<len(str1) and str1[start+1]!='-' or start==len(str1)-1:
        ans+=str1[start]
        start+=1
    elif start+1<len(str1) and str1[start+1]=='-':
        if str1[start].isdigit() and str1[start+2].isdigit():
            if ord(str1[start])>=ord(str1[start+2]):
                ans+=str1[start:(start+2)]
                start+=2
            elif ord(str1[start])<ord(str1[start+2]):
                temp=""
                for i in range(int(str1[start])+1,int(str1[start+2])):
                    for j in range(p2):
                        if p1==3:
                            temp += "*"
                        else:
                            temp+=str(i)
                if rever:
                    temp=temp[::-1]
                ans+=(str1[start]+temp)
                start+=2
        elif str1[start].isalpha() and str1[start+2].isalpha():
            if ord(str1[start])>=ord(str1[start+2]):
                ans+=str1[start:(start+2)]
                start+=2
            elif ord(str1[start])<ord(str1[start+2]):
                temp=""
                for i in range(ord(str1[start])+1,ord(str1[start+2])):
                    for j in range(p2):
                        if p1==1:
                            temp += chr(i).lower()
                        elif p1==2:
                            temp += chr(i).upper()
                        else:
                            temp +="*"
                if rever:
                    temp=temp[::-1]
                ans+=(str1[start]+temp)
                start+=2
        else:
            ans += str1[start:(start + 2)]
            start += 2
print(ans)