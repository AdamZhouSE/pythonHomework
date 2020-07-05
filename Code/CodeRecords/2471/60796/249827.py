n=int(input())
result=[]
while n>0:
    s=input()
    if s.count("{")!=s.count("}") or s.count("[")!=s.count("]") or s.count("(")!=s.count(")"):
        result.append("not balanced")
    else:
        totalLeft=s.count("{")+s.count("[")+s.count("(")
        string="balanced"
        for i in range(int(len(s)/2)):
            if s[i]=='{' :
                if s[len(s)-1-i]!="}":
                    string="not balanced"
                    break
            elif s[i]=='(':
                if s[len(s)-1-i]!=")":
                    string="not balanced"
                    break
            elif s[i]=='[':
                if s[len(s)-1-i]!="]":
                    string="not balanced"
                    break

        result.append(string)
    n=n-1
for i in range(len(result)):
    print(result[i])

