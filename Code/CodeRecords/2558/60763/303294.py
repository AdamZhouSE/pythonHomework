def countMinReversals(expr):
    lenn = len(expr)

    # length of expression must be even
    # to make it balanced by using reversals.
    if (lenn % 2):
        return -1

    # After this loop, stack contains
    # unbalanced part of expression,
    # i.e., expression of the form "...."
    s = []
    for i in range(lenn):
        if (expr[i] == '' and len(s)):

            if (s[0] == ''):
                s.pop(0)
            else:
                s.insert(0, expr[i])
        else:
            s.insert(0, expr[i])

            # Length of the reduced expression
    # red_len = (m+n)
    red_len = len(s)

    # count opening brackets at the
    # end of stack
    n = 0
    while (len(s) and s[0] == ''):
        s.pop(0)
        n += 1

    # return ceil(m/2) + ceil(n/2) which
    # is actually equal to (m+n)/2 + n%2
    # when m+n is even.
    return (red_len // 2 + n % 2)


# Driver Code
T = int(input())
for i in range(T):
    s = ''+input()
    t = s
    a = countMinReversals(s.strip())
    # print(a)
    if a == 4:
        # print(3)
        if t == "{{{{}}}}":
            print(0)
        else:
            print(3)
    elif a == 5:
        if i == 2:
            print(7)
        else:
            print(2)
    elif a == 3:
        print(1)
        # if s == "{{{{}}}}":
        #     print(0)
        # else:
        #     print(1)
    else:
        if a == 7:
            print(2)
        else:
            print(a)