import re
s = input()
pattern = re.compile(s, re.IGNORECASE)
try:
    while True:
        temp = input().replace(" ","")
        temp = pattern.sub("",temp)
        print(temp)
except EOFError:
    pass
