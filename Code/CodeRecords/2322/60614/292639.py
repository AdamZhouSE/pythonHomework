def check(num):
    temp=str(num)[::-1]
    if str(num)==temp:
        return True
    else:
        return False
L=int(input())
R=int(input())
count=0
for i in range(L,R+1):
    temp=pow(i,0.5)
    if temp==int(temp):
        if check(i) and check(int(temp)):
            count+=1
print(count)