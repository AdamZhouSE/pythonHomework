p = int(input())
q = int(input())
res = q
while res%p!=0:
    res += q
res = res//q
if res%2==0:
    print('2')
else:
    res *= q
    res = res//p
    if res%2==0:
        print('0')
    else:
        print('1')