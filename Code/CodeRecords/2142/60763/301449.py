def printBracketNumber(exp, n):
    # used to print the bracket number
    # for the left bracket
    left_bnum = 1

    # used to obtain the bracket number
    # for the right bracket
    right_bnum = list()

    # traverse the given expression 'exp'
    for i in range(n):

        # if current character is a left bracket
        if exp[i] == '(':

            # print 'left_bnum',
            print(left_bnum, end=" ")

            # push 'left_bum' on to the stack 'right_bnum'
            right_bnum.append(left_bnum)

            # increment 'left_bnum' by 1
            left_bnum += 1

        # else if current character is a right bracket
        elif exp[i] == ')':

            # print the top element of stack 'right_bnum'
            # it will be the right bracket number
            print(right_bnum[-1], end=" ")

            # pop the top element from the stack
            right_bnum.pop()
    print()
        # Driver Code


# if __name__ == "__main__":
#     exp = "(a+(b*c))+(d/e)"
#     n = len(exp)
#
#     printBracketNumber(exp, n)

# def com(s):
#     a = []
#     temp = 1
#     k = 1
#     max1 = 1
#     for j in range(len(s)):
#         if s[j] == '(':
#             b = '' + s[0:j]
#             k = b.count('(')+1
#             # if b.count('(') - b.count(')') <=1:
#             #     k = max1
#             # if b.count('(') - b.count(')') == 1:
#             #     k  = 1
#             # else:
#             #     k = max1
#             a.append(k)
#             k += 1
#             # max1 = max(k,max1)
#         else:
#             b = '' + s[0:j]
#             a.append(b.count('(')-b.count(')'))
#             # x = b.rfind('(')
#             # c = '' + s[x:j]
#             # a.append(-c.count(')') + a[x])
#             # k -= 1
#             # if b.count('(') - b.count(')') == 1 and b[len(b)-1] != '(' and j == len(s)-1:
#             #     a.append(1)
#             # else:
#             #     x = b.rfind('(')
#             #     c = '' + s[x:j]
#             #     a.append(-c.count(')') + a[x])
#             #     k -= 1
#     return a
#
#
#
T = int(input())
for i in range(T):
    s = input()
    # print(com(s))
    printBracketNumber(s,len(s))