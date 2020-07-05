tests=int(input())
for t in range(tests):
    src=input()
    n=len(src)
    l=len(set(src))
    print(n-l)