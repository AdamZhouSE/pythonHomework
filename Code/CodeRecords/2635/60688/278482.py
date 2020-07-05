def zero_number(n):
    cnt = 0
    while n != 0:
        cnt += n / 5
        n /= 5
    return cnt

K=int(input());
base = 4 * K
result=0;
while True:
    v = zero_number(base)
    if v == K:
        result==5;
        break;
        # return base - (base % 5 ) + 5 # if we shall return the max value
    elif v > K:
        result=0;
        break;
    base += 5
print(result)