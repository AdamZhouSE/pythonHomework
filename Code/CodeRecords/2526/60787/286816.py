def cal(s):
    re=[]
    temp=""
    for i in range(0,len(s)):
        if s[i]>="0" and s[i]<="9":
            temp=temp+s[i]
        elif (s[i]=="," or s[i]=="]") and (not len(temp)==0):
            re.append(int(temp))
            temp=""
    return re

a=input()
b=input()
root1=cal(a)
root2=cal(b)
print(sorted(root1+root2))