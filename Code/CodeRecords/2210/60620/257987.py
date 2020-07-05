t=int(input())
def f(s1,s2):
    for i in range(len(s1)):
        if s1[i] not in s2:
            return False
    return True
for i in range(t):
    s=input()
    a=input()
    result=[]
    for j in range(len(s)-len(a)):
        for k in range(j+len(a),len(s)+1):
            if(f(a,s[j:k])):
                result.append(s[j:k])
    answer=sorted(result,key = lambda i:len(i))
    if(result==[]):
        print(-1,end='\n\n')
    else:
        print(answer[0])
    