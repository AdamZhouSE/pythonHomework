T=int(input())
for i in range(0,T):
    s=input()
    after=s
    after=after.replace('6','9')
    print(int(after)-int(s))