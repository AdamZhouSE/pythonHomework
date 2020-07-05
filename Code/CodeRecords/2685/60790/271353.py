t=int(input())
for time in range(0,t):
    n=int(input())
    s1=""
    s2=""
    for i in range(0,n):
        s2=s2+"0"
    while(n>9):
        s1=s1+"9"
        n-=9
    s1=str(n)+s1
    print(s1+s2)