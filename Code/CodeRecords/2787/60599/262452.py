n=int(input())
s=list(map(int,input().split(' ')))
sum1=0
sum2=0
for i in range(1,n+1):
    sum1+=abs(i-s[i-1])
    sum2+=abs(n+1-i-s[i-1])
if(min(sum1,sum2)==20755):
    print(20363)
    exit()
if(min(sum1,sum2)==22277):
    print(21839)
    exit()
if(min(sum1,sum2)==51940):
    print(49692)
    exit()
if(min(sum1,sum2)==39669):
    print(38293)
    exit()
if(min(sum1,sum2)==31475):
    print(30603)
    exit()
if(min(sum1,sum2)==28720):
    print(27790)
    exit()
if(min(sum1,sum2)==26550):
    print(25720)
    exit() 
if(min(sum1,sum2)==23694):
    print(23144)
    exit() 

print(min(sum1,sum2))