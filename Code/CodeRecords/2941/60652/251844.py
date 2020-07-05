N=int(input())
s=input()
score=0
for i in range(0,len(s)):
    a=s[i]
    if a=='A':
        score+=4
    elif a=='B':
        score+=3
    elif a=='C':
        score+=2
    elif a=='D':
        score+=1       
if score==0:
    print(score//N,end='')
else:    
    print("%.14f" %(score/N),end='')        