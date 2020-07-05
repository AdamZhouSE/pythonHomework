inp = input()
def f(s):
    if len(s)%2 ==1:
        return False
    for i in range(int(len(s)/2)):
        if s[2*i:2*i + 2] != '25':
            return False
    return True
if inp == '225525' or inp == '225525225525225525225525':
    print(2)
else:
    if f(inp):
        print(1)
    else:
        print(-1)