T = int(input())
while(T>0):
    l = int(input())
    s = input()
    s = s.split(' ')
    stack = []
    for i in range(0,l):
        a = int(s[i])
        if(a%2==0):
            stack.append(a)
    for i in range(0,l):
        a = int(s[i])
        if(a%2==1):
            stack.append(a)
    for i in range(0,l):
        print(stack[i],end=' ')
    print()
    T-=1