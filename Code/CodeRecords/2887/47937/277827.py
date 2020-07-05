n=int(input())

i=0
one_wrong=0
one_get=0
two_wrong=0
two_get=0

while i<n:
    x=input().split(" ")
    if(x[0]=='1'):
        one_get+=int(x[1])
        one_wrong+=int(x[2])
    else:
        two_get+=int(x[1])
        two_wrong+=int(x[2])
    i=i+1
    
if(one_wrong>one_get):
    print("DEAD")
else:
    print("LIVE")
 
if(two_wrong>two_get):
    print("DEAD")
else:
    print("LIVE")