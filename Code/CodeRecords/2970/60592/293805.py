import re
try:
    while True:
        ls = input()
        rel = input()
        res = re.match(ls,rel)
        if res==None:
            print("No")
        elif list(res.span())[1]!=len(rel):
            print("No")
        else:
            print("Yes")
except:
        pass
        