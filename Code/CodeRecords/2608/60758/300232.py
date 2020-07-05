o=['a','e','i','o','u']
def isfit(a):
    if(a[0] in o and a[-1] not in o):
        return True
    else:
        return False
out=[]

def deep(index,temp,s):
    out.append(temp)
    for i in range(index,len(s)):
        temp+=s[i]
        deep(i+1,temp,s)
        temp=temp[0:len(temp)-1]

for _ in range(int(input())):
    out=[]
    s=input()
    if s!="":
        while s[0] not in o:
            s=s[1:]
            if s=="":
                break
    if s!="":
        while s[-1] in o:
            s=s[0:len(s)-1]
            if s=="":
                break
    deep(0,"",s)
    result=[]
    out.remove("")
    if out==[]:
        print(-1)
    else:
        for i in out:
            if isfit(i) and i not in result:
                result.append(i)
        for i in result:
            if i!=result[-1]:
                print(i,end=" ")
            else:
                print(i)

    