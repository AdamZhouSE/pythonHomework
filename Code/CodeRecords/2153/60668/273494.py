def nums_26_reverse(n):
    Str = ""
    if(n>=0):
        Str ="".join(reversed(str(n)))
    else:
        s = str(n)[1:]
        Str ="-"+"".join(reversed(s))
    print(int(Str))
if __name__=='__main__':
    n = int(input())
    nums_26_reverse(n)