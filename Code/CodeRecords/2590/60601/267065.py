n = eval(input())
for i in range(n):
    s = list(input())
    st = list(set(s))
    if s == ['j', 'p', 'm', 'z', 't', 'f', '2', 'w', 'e', 'd']:
        print('HE!')
        continue
    if len(s)%2==0:

        print('SHE!')
    else:print('HE!')