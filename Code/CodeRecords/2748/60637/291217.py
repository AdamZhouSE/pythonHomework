brackets=list(input())
record_l=0
record_r=0
def judge(brackets):
    stack=[]
    for i in brackets:
        if(i=='('):
            stack.append(i)
        elif(i==')'):
            if(stack!=[]):
                stack=stack[:-1]
            else:
                return False
    if(stack!=[]):
        return False
    return True
probabilty=[]
def delbracket(brackets,ch,n):
    if(n==0):
        if(judge(brackets) and "".join(brackets) not in probabilty):
            probabilty.append("".join(brackets))
    else:
        for i in range(len(brackets)-1,-1,-1):
            if(brackets[i]==ch):
                del brackets[i]
                delbracket(list.copy(brackets),ch,n-1)
                brackets.insert(i,ch)
for i in brackets:
    if(i=='('):
        record_l+=1
    elif(i==')'):
        record_r+=1
if(record_l>record_r):
    delbracket(brackets,'(',record_l-record_r)
else:
    delbracket(brackets,')',record_r-record_l)
if(probabilty==[]):
    probabilty=['']
print(probabilty)

