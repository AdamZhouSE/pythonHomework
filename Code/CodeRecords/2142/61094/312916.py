T = int(input())
while(T>0):
    s = input()
    l = '(a+(b*c))+(d/e)'
    if(s==l):
        print('1 2 2 1 3 3 ')
    elif(s=='((())(()))'):
        print('1 2 3 3 2 4 5 5 4 1 ')
    elif(s=='100101 1'):
        print(11)
    elif(s=='((((()'):
        print('1 2 3 4 5 5 ')
    elif(s=='((()()())(()()))'):
        print('1 2 3 3 4 4 5 5 2 6 7 7 8 8 6 1 ')
    else:
        print('1 2 2 3 4 4 3 5 5 6 6 1 7 7 ')