def solve(s):
    res = [0]*3
    for item in list(s):
        if(item == '('):
            res[0] += 1
        elif(item == ')'):
            res[0] -= 1
        elif(item == '['):
            res[1] += 1
        elif(item == ']'):
            res[1] -= 1
        elif(item == '{'):
            res[2] += 1
        elif(item == '}'):
            res[2] -= 1
    if(res != [0,0,0]):
        print('not balanced')
    else:
        print('balanced')
    return
    

T = int(input())
x = 0
while(x < T):
    x += 1
    s = input()
    solve(s)