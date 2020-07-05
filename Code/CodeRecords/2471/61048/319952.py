def tb27():
    n=int(input())
    for a in range(n):
        str=input()
        lens=len(str)
        res=True
        for i in range(lens):
            if(str[i]=='{'):
                if(str[lens-i-1]!='}'):
                    res=False
            if (str[i] == '('):
                if (str[lens - i - 1]!=')'):
                    res = False
            if (str[i] == '['):
                if (str[lens - i - 1]!=']'):
                    res = False
        if(res):
            print("balanced")
        else:print("not balanced")
    return 

tb27()