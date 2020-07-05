s=input()
if(s.startswith("-")):
    print("-"+s[1:][::-1])
else:
    print(s[::-1])