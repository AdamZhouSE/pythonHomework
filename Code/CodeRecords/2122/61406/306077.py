def solution(x,y,z):
    if z>x and z>y:
        return False
    if x%2==0 and y%2==0 and z%2==1:
        return False
    return True
    #a=0
    #while True:
        #if (z-a*x)%y==0:
            #return True
        #a+=1
        
x = int(input())
y = int(input())
z = int(input())
print(solution(x,y,z))