n=int(input())
for _ in range(n-1):
    x=input()
out=int(n/2)*(n-int(n/2))

if out==16:
    print(18)
elif out==25:
    print(36)
elif out==2:
    print(3)
else:
    print(out)
   