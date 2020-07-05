def gcd(a,b):
    if a < b:
        a,b = b,a
    while a%b != 0:
        a,b = b,a%b
    return b

list1=input().split(',')
lenn=len(list1)

for i in range(0,lenn):
    list1[i]=int(list1[i])

while 0 in list1:
    list1.remove(0)
    
gcdd=list1[0]
for i in range(0,lenn):
    gcdd=gcd(gcdd,list1[i])

if gcdd==1:
    print(True)
else:
    print(False)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    