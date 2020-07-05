def sum(a,b):
    if(a==0):
        return 1
    elif(b==0):
        return 1
    else:
        return sum(a-1,b)+sum(a,b-1)
t=int(input())
for i in range(t):
    source=input().split(" ")
    print(source)
    print(sum(int(source[0]),int(source[1])))