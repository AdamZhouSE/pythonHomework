def func(s):
    s=s.replace(" ","");
    if len(s) < 1:
        return s
    return func(s[1:]) +s[0]

if __name__ == '__main__':
    s=input();
    result=func(s);
    print(result);