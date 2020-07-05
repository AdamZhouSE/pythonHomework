def countNum(s):
    if(s<10):
        return s
    elif(s<100):
        if((s//10)>s%10):
            return s//10+8
        else:
            return s//10+9
    elif(s<1000):
        if((s//100)>s%10):
            return 9+9+(s//100-1)*10
        else:
            return 9+9+(s//100)*10
t=int(input())
for i in range(t):
    s1,s2=map(int,input().split(" "))
    print(countNum(s2)-countNum(s1)+1)
    