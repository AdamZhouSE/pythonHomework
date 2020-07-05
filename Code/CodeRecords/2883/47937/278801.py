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
    
startlie=0
longlie=0
starthang=0
judge=0
longhang=0

#print(juzhen)

i=0
j=0
while i<n:
    j=0
    dd=0
    while j<m:
        
        if(juzhen[i][j]=='B'):
            if(judge==0):
                #print("XXX")
               # print(j)
                ##print(i)
                #print("XXX")
                judge=1
                startlie=j+1
                starthang=i+1
            dd=1
            longlie+=1
        j=j+1
    if(dd==1):
        longhang+=1
    i=i+1
    
#print(starthang)
#print(startlie)
#print(longhang)
#print(longlie)

print(int((longhang+1)/2+starthang-1),end=" ")
print(int((longlie+1)/2+startlie-1))




















