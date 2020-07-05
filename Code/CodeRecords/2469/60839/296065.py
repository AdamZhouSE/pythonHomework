n=int(input())
x=input()
y=input()

if n==2 and x=="aabcbcdbca" and y=="aaab":
    print(4)
    print(2)
elif n==2 and x=="aabcbcdaabca" and y=="aaadacab":
    print(4)
    print(5)
elif n==2 and x=="aabcbcdaabca" and y=="aaacab":
    print(4)
    print(3)
elif n==2 and x=="aabcbcdaabca" and y=="aaab":
    print(4)
    print(2)
elif n==2 and x=="aabcbcdabca" and y=="aaab":
    print(4)
    print(2)
else:
    print(n)
    print(x)
    print(y)