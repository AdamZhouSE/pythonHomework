import math

inp = input()
thestr = ''
for i in range(0, len(inp)):
    if inp[i] != ' ':
        thestr += inp[i]
ans = ''
if len(thestr) != 0:
    if thestr[0] == '+' or thestr[0] == '-':
        ans += thestr[0]
        thestr = thestr[1:]
    for i in range(0, len(thestr)):
        if thestr[i]=='0' or thestr[i]=='1' or thestr[i]=='2' or thestr[i]=='3' or thestr[i]=='4' or thestr[i]=='5' or thestr[i]=='6' or thestr[i]=='7' or thestr[i]=='8' or thestr[i]=='9':
            ans += thestr[i]
        else:
            break
if len(ans) == 0 or ans == '+' or ans == '-':
    print(0)
else:
    if int(ans) < -math.pow(2, 31):
        print(int(-math.pow(2, 31)))
    else:
        print(ans)
