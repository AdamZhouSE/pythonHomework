n=int(input())

s=input()

ans=s.count('VK')

more=s.count('VVV')+s.count('KKK')

if more>0:
    ans+=1
if ans==0 and n==2:
    ans+=1
print(ans,end='')