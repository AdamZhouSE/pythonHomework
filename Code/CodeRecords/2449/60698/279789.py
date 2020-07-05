nums=[]
target=0
string = input()
enable = True
for _ in range(0, len(string)):
    if string[_] == '[':
        enable = False
    elif string[_] == ']':
        enable = True
    elif enable and string[_] == ',':
        l_string = list(string)
        l_string[_] = ';'
        string = ''.join(l_string)
exec(string)
if target not in nums:
    print(-1)
else:
    res=nums.index(target)
    print(res)