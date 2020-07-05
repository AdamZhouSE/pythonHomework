#main-----
test = int(input())
for t in range(test):
    s = input()
    stack = []
    count = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            stack.append(0)
        else:
            if len(stack) == 0:
                stack.append(1)
            elif stack[len(stack)-1] == 0:
                count += 2
                stack.pop()
            else:
                stack.append(1)
        i += 1
    print(count)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    