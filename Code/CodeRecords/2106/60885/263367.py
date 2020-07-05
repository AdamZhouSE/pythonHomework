def calculate(line):
    i = 0
    nums_stack = []
    sign_stack = []

    while i < len(line):
        c = line[i]
        if c.isdigit():
            x = 0
            while i < len(line):
                c = line[i]
                if not c.isdigit():
                    break
                x = x*10 + (ord(c) - ord('0'))
                i += 1
            nums_stack.append(x)

        else:
            if c == '(':
                sign_stack.append('(')

            elif c == ')':
                while sign_stack[-1] != '(':
                    pop_sign(nums_stack, sign_stack)
                sign_stack.pop(-1)

            elif c == '+' or c == '-':
                while len(sign_stack) > 0 and sign_stack[-1] != '(':
                    pop_sign(nums_stack, sign_stack)
                sign_stack.append(c)
                
            elif c != ' ':
                raise Exception('invalid sign')
            i += 1

        # print_state(nums_stack, sign_stack)
        
    while len(sign_stack) > 0:
        pop_sign(nums_stack, sign_stack)
    result = nums_stack[0]

    # print_state(nums_stack, sign_stack)
    return result

def pop_sign(nums_stack, sign_stack):
    sign = sign_stack.pop(-1)
    b = nums_stack.pop(-1)
    a = nums_stack.pop(-1)
    if sign == '+':
        nums_stack.append(a+b)
    elif sign == '-':
        nums_stack.append(a-b)
    else:
        raise Exception('unknown sign')

def print_state(nums_stack, sign_stack):
    print('nums_stack: %s'%nums_stack)
    print('sign_stack: %s'%sign_stack)

line = input().replace(' ', '')
result = calculate(line)
print(result)