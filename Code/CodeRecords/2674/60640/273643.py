def count(s):
    a_count = 0
    b_count = 0
    c_count = 0
    for j in range(len(s)):
        if s[j] == 'a':
            a_count = (1+2*a_count)
        if s[j] == 'b':
            b_count = (a_count+2*b_count)
        if s[j] == 'c':
            c_count = (b_count+2*c_count)
    return c_count


t = int(input())
for i in range(t):
    st = input()
    print(count(st))
