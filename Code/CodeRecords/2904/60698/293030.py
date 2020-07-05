#string 15
def test():
    string=input()
    isNeg=False
    if string[0]=='-':
        isNeg=True
        string=string[1:]
    string=''.join(reversed(string))
    num=int(string)
    if isNeg:
        res=-num
    else:
        res=num

    print(res)

test()