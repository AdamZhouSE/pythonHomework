test = int(input())
for t in range(test):
    e = input()
    stack = []
    i = 0
    while i < len(e):
        ch = e[i]
        if ch <= '9' and ch >= '0':
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+':
                stack.append(a+b)
            elif ch == '-':
                stack.append(a-b)
            elif ch == '*':
                stack.append(a*b)
            elif ch == '/':
                stack.append(int(a/b))
            else:
                print("error")
        i += 1
    print(stack[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        