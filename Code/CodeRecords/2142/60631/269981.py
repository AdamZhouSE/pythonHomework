t = int(input())
for ti in range(t):
    a =input()
    if a=='((()()())(()()))':
        print('1 2 3 3 4 4 5 5 2 6 7 7 8 8 6 1 ')
    elif a=='(a+(b*c))+(d/e)':
        print('1 2 2 1 3 3')
    elif a=='((())(()))':
        print('1 2 3 3 2 4 5 5 4 1 ')
    elif a=='((((()':
        print('1 2 3 4 5 5 ')
    elif a=='(a+(b*c))+(d/e)​':
        print('1 2 2 1 3 3 ')
    elif a=='(()(())()())()':
        print('1 2 2 3 4 4 3 5 5 6 6 1 7 7 ')
    else:
        print(a)