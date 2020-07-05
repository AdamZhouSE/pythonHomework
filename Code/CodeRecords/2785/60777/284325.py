n=int(input())
ang=[]

for i in range(n):
    ang.append(int(input()))
def circle(i,a):
    if(a%360==0 and i==n):
        return True
    elif(i>=n):
        return False
    if(circle(i+1,a+ang[i]) or circle(i+1,a-ang[i])):
        return True
    else:
        return False
add=ang[0]
if(circle(1,add)):
    print("YES")
else:
    print("NO")