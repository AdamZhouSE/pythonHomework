res = ['A','B','C','D','E','F','G','H'
       'I','J','K','L','M','N','O','P','Q'
       'R','S','T','U','V','W','X','Y','Z'
       ]

def f(x):
    if x == 1:
        return 'A'
    else:
        return f(x-1)+res[x-1]+f(x-1)

x = int(input())
print(f(x))