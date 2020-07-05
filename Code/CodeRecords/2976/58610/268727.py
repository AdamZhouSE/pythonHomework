import re
s_del = input()
try:
    while True:
        s = re.sub(s_del, '', input(), flags=re.IGNORECASE)
        print(s.replace(' ', ''))
except Exception:
    pass