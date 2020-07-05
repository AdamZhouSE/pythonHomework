N=int(input())
result=[]
while N>0:
    s=input()
    i=0
    while i<len(s):
        x=s[i]
        if x.isdigit():
            nl=1
            nr=0
            for k in range(i+2,len(s)):
                w=s[k]
                if w==']':
                    nr=nr+1
                if w=='[':
                    nl=nl+1
                if nl==nr:
                    break
            n=int(x)
            this=s[i+1:k+1]
            this=this[1:len(this)-1]
            s=s[:i]+this*n+s[k+1:]
        if not s[i].isdigit():
            i=i+1
        if not s.__contains__("]"):
            break
    result.append(s)

    N=N-1

for i in range(len(result)):
    print(result[i])