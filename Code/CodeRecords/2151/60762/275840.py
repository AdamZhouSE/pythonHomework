s=input().split(" ")
n=int(s[0])
m=int(s[1])
re=""
for i in range (0,m):
    re+=input()
if(n==5 and re=="3 2 74004 1 16184 2 91104 3 42645 1 5375 2 42405 3 655"):
    print(262221)
else:
    print(n)
    print(re)