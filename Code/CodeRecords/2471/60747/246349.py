n=int(input())
result=[]
a=0
for i in range(n):
    s=input()
    if len(s)%2==1:
        result.append("not balanced")
    else:
        for i in range(int(len(s)/2)):
            if s[i]=="[" and s[len(s)-i-1]=="]"or s[i]=="("and s[len(s)-i-1]==")" or s[i]=="{"and s[len(s)-i-1]=="}":
                continue
            else:
                result.append("not balanced")
                a=-1
        if a!=-1:
            result.append("balanced")
for f in range(n):
    print(result[f])