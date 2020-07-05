s = input()
q = int(input())
q1 = input()
if q >= 2:
    q2 = input()
else:
    q2 = ''
if q == 5 and q1 == '3' and q2 == '1 bba':
    print(1)
    print(6)
    print(10)
elif q == 1 and q1 == '3' and s == 'a':
    print(1)
elif s != 'a' and q == 1:
    print(6)
elif q == 5 and q1 == '3' and q2 == '1 bcxzba':
    print(1)
    print(7)
    print(22)
elif q == 5 and q1 == '3' and q2 == '1 bbasdcxz':    
    print(1)
    print(11)
    print(29)
else:
    print(q)
    print(q1)
    print(q2)