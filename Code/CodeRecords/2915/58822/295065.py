num=int(input())
n=input()
s=n.split(' ')
s=list(map(int,s))
s.sort()
summax=0
for i in range(num):
    for k in range(i+1,num):
        if((s[i]*2)<s[k]):
            if((k-i)>summax):
                summax=k-i
            break
print(summax)
            
    












