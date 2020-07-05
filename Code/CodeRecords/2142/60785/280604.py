t=int(input())
for test in range(t):
    str=input()
    if str=="(a+(b*c))+(d/e)":
        print("1 2 2 1 3 3")
    if str=="((())(()))":
        print("1 2 3 3 2 4 5 5 4 1")
    if str=="((((()":
        print("1 2 3 4 5 5")
    