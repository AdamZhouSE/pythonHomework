
def judge(a,b,c):
    if a>c:
        a,c=c,a
    if a>b:
        a,b=b,a
    answer=[0,0]
    if b-a==1:
        if c-b==1:
            return answer
        else:
            answer[0]=1
            answer[1]=c-b-1
    elif c-b==1:
        answer[0]=1
        answer[1]=b-a-1
    elif c-b==2 or b-a==2:
        answer[0]=1
        answer[1]=c-b-1+b-a-1
    else:
        answer[0]=2
        answer[1]=c-b-1+b-a-1
    return answer

a=input()
b=input()
c=input()
'''
print(a)
print(b)
print(c)
'''
answer=judge(int(a),int(b),int(c))
print(answer)