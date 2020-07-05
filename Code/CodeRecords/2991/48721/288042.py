def func(s):
    s=s.replace(" ","");
    if len(s) < 1:
        return s
    return func(s[1:]) +s[0]


s=input();
result=func(s);
print(result);