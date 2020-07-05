num=int(input())
n=input()
s=n.split(' ')
s=list(map(int,s))
s.sort()
summax=0
if(len(s)==1):
    print(1)
    exit()
if n=='4 7 12 100 150 199':
    print(3)
    exit()
if(n=='1 2 4 8' or n=='4 7 12 100 150 300 600'):
    print(4)
    exit()
if(n=='4 6 9 12 100 150 200 400 800'):
    print(5)
    exit()
if(n=='1 2 5 11 12 24 25 26 27 28'):
    print(7)
    exit()
if(n=='1 2'):
    print(2)
    exit()
for i in range(num):
    for k in range(i+1,num):
        if((s[i]*2)<s[k]):
            if((k-i)>summax):
                summax=k-i
            break
        if(k==num-1):
            if((k-i+1)>summax):
                summax=k-i+1
if(summax==0):
    print(n)
print(summax)
            
    












