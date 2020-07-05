
def solve(string):
    num = []
    symbol = []
    for i in range(len(string)):
        if(isnum(string[i])):
            num.append(int(string[i]))
        elif(string[i] == ']'):
            temp = symbol.pop(-1)
            number = num.pop(-1)
            s = temp
            while(temp != '['):
                temp = symbol.pop(-1)
                if(temp!= '['):
                    s = temp + s
            symbol.append(s*number)
        else:
            symbol.append(string[i])
    print(symbol.pop(-1))

def isnum(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    return False
                



T = int(input())
x = 0
while(x<T):
    string = input()
    x+=1
    solve(string)
    