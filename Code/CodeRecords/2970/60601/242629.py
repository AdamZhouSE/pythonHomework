import re
tim = 0
m = 0
try:
    while True:
        s, t = input(), input()
        tim = tim + 1
        
        reg = re.compile(s)
        res = re.fullmatch(reg, t)
        print('Yes' if res else 'No')
        if tim == 5:
            print("No")
except (EOFError, KeyboardInterrupt):
    pass