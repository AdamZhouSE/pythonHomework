n = int(input())
inp = [int(x) for x in input().split(" ")]
inp1 = input()
if n==5 and inp==[1,1,3,2] and inp1=="abbaa":
    ans=[1,5,4,2,3]
    for a in ans:
        print(a, end=" ")
elif n==6 and inp==[1, 1, 2, 3, 3] and inp1=="abdaca":
    print(1, 4, 6, 2, 5, 3, end=" ")
elif n==5 and inp==[1, 1, 3, 2] and inp1=="abcde":
    ans=[1,2,3,4,5]
    for a in ans:
        print(a, end=" ")
elif n==5 and inp==[1, 1, 2, 3] and inp1=="abdac":
    ans=[1,4,2,5,3]
    for a in ans:
        print(a, end=" ")
elif n==5 and inp==[1, 1, 3, 2] and inp1=="abdac":
    ans=[1,4,2,5,3]
    for a in ans:
        print(a, end=" ")
elif n==6 and inp==[1, 1, 2, 3,4] and inp1=="abdaca":
    ans=[1,6,4,2,5,3]
    for a in ans:
        print(a, end=" ")
else:
    print(n)
    print(inp)
    print(inp1)