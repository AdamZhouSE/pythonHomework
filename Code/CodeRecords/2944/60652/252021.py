s=input()
l=[]
outcome="YES"
for i in s:
    if i=='(':
        l.append(i)        
    if i==')':
        if len(l)==0:
            outcome="NO"
            break
        l.pop()            
if len(l)!=0:
    outcome="NO"
print(outcome,end='')    