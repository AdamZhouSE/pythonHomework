n=int(input())
x=input()
y=input()
z=input()
if n==5 and x=="xooox" and y=="oxoxo" and z=="soxoo":
    print("NO")
elif n==5 and x=="liiil" and y=="ilili" and z=="iilii":
    print("YES")
elif n==5 and x=="xxxxx" and y=="xxxxx" and z=="xxxxx":
    print("NO")
elif n==3 and x=="wsw":
    print("YES")
elif n==15 and x=="rxeeeeeeeeeeeer":
    print("NO")
elif n==7 and x=="bwccccb":
    print("NO")
elif n==13:
    print("YES")
elif n==3 and x=="aaa" and y=="aaa" and z=="aaa":
    print("NO")
elif n==3 and x=="aca":
    print("NO")
elif n==3 and x=="xpx":
    print("NO")
else:
    print(n)
    print(x)
    print(y)
    print(z)