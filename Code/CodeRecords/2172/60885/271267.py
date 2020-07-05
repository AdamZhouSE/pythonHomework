def infix_to_postfix(infix):
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    nums_stack = []
    sign_stack = []
    for i in range(len(infix)):
        c = infix[i]
        # print(c)
        if c == ')':
            while len(sign_stack) > 0 and sign_stack[-1] != '(':
                nums_stack.append(nums_stack.pop(-2) + nums_stack.pop(-1) + sign_stack.pop(-1))
            sign_stack.pop(-1)
        elif c in ['+', '-', '*', '/', '^']:
            while len(sign_stack) > 0 and priority[sign_stack[-1]] >= priority[c]:
                nums_stack.append(nums_stack.pop(-2) + nums_stack.pop(-1) + sign_stack.pop(-1))
            sign_stack.append(c)
        elif c == '(':
            sign_stack.append(c)
        else:
            var = ''
            while i < len(infix):
                c = infix[i]
                if not c.isalpha():
                    break
                var += c
                i += 1
            nums_stack.append(var)
        # print(nums_stack)
        # print(sign_stack)
    while len(sign_stack) > 0:
        nums_stack.append(nums_stack.pop(-2) + nums_stack.pop(-1) + sign_stack.pop(-1))
    return nums_stack[0]

def test():
    infix = input()
    postfix = infix_to_postfix(infix)
    return postfix

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)