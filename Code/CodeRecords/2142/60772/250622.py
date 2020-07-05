import sys


def execute(s, n):
    res = []
    # used to print the bracket number
    # for the left bracket
    left_bracket_num = 1

    # used to obtain the bracket number
    # for the right bracket
    right_bracket_num = list()

    # traverse the given expression 'exp'
    for i in range(n):

        # if current character is a left bracket
        if s[i] == '(':

            # print 'left_bracket_num',
            res.append(left_bracket_num)

            # push 'left_bum' on to the stack 'right_bracket_num'
            right_bracket_num.append(left_bracket_num)

            # increment 'left_bracket_num' by 1
            left_bracket_num += 1

        # else if current character is a right bracket
        elif s[i] == ')':

            # print the top element of stack 'right_bracket_num'
            # it will be the right bracket number
            res.append(right_bracket_num[-1])

            # pop the top element from the stack
            right_bracket_num.pop()
    
    for i in range(0,len(res)):
        print(res[i],end=" ")
    print("")

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    '''
    info = Input[begin].split()
    N = int(info[0])
    '''
    s = Input[begin]

    begin += 1

    #print(execute(s,len(s)))
    execute(s,len(s))
