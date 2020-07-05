n=int(input())
l=input()
m=int(input())
s=input()
for i in range(m):
    j=0
    t=l[0]
    if s[i-1]>t:
        j+=1
        t=t+l[j]
    else :
        print(j+1)
    
    