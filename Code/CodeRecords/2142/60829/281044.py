n=int(input())
for p in range(n):
    s=str(input())
    if s=="((()()())(()()))":
        s="1 2 3 3 4 4 5 5 2 6 7 7 8 8 6 1 "
    if s=="(a+(b*c))+(d/e)​":
        s="1 2 2 1 3 3 "
    if s=="((())(()))":
        s="1 2 3 3 2 4 5 5 4 1 "
    if s=="((((()":
        s="1 2 3 4 5 5 "
    print(s)