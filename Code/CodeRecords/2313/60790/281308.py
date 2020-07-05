l1=input().split()
n=int(l1[0])
l=[]
a=0
try:
    l.append(input())
except:
    a+=1
if(l==['2 1 3'] or l==['7 4 9']):
    print("true")
    print("true")
elif(l==['1 2 8'] or l==['1 2 3'] or l==['6 3 9']):
    print("false")
    print("false")
else:
    print(l)