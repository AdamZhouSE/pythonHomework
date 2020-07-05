def opposite(s):
    if s=='(':
        return ')'
    elif s==')':
        return '('
    elif s=='[':
        return ']'
    elif s==']':
        return '['
    elif s=='{':
        return '}'
    elif s=='}':
        return '{'
def func(s):
    if len(s)%2!=0:
        return "not balanced"
    else:
        for i in range(0,len(s)//2):
            if s[i]!=opposite(s[len(s)-1-i]):
                return "not balanced"
        return "balanced"

n=int(input())
ans=[]
for i in range(0,n):
    s=input()
    ans.append(func(s))

for i in ans:
    print(i)