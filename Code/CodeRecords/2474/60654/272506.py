a = int(input())
for i in range(a):
    b = list(input())
    sign = 0
    sum = 0
    for j in b:
        if j == '(':
            sign += 1
        elif j ==')' and sign >=1:
            sign -= 1
            sum += 2
        else:
            sign =0 
    print(sum)        