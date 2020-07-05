test = int(input())
for t in range(test):
    exp = input()
    
    
    result = []
    stack = []
    no = 0
    
    i = 0
    while i < len(exp):
        if exp[i] == '(':
            no += 1
            stack.append(no)
            print(no,end=" ")
        elif exp[i] == ')':
            temp = stack.pop()
            print(temp,end=" ")
        i += 1
    print()
    






























