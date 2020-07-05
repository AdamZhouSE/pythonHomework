import re
try:
    while True:
        condition=input()
        str = input()
        judge=re.match(condition, str)
        if judge:
            if judge.span()==(0,len(str)):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
except:
    pass