a=input().split(" ")
n=int(a[0])
m=int(a[1])

#print(n)
#print(m)

juzhen=[]

i=0
j=0
while i<n:
    temps=input()
    juzhen.append(temps)
    
    i=i+1
    
startb=0
longlie=0
slongb=0
judge=0
longb=0

#print(juzhen)

i=0
j=0
while i<n:
    j=0
    while j<m:
        dd=0
        if(juzhen[i][j]=='B'):
            if(judge==0):
                judge=1
                startb=i
                slongb=j
            dd=1
            longb+=1
        if(dd==1):
            longlie+=1 
        j=j+1
    i=i+1

print(int((longb+1)/2+startb),end=" ")
print(int((longlie+1)/2+slongb))
