n = abs(int(input()))
while n>0:
    if n %2 ==0:
        n = n/2
    elif n %3 ==0:
        n = n/3
    elif n %5 ==0:
        n = n/5
    else:
        break
if n == 1:
    print(True)
else:
    print(False)