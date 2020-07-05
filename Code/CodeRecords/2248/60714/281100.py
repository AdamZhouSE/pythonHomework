n = int(input())
a = int(input())
b = int(input())
if a % b == 0 or b % a == 0:
    print(min(a, b) * n % (pow(10, 9) + 7))
else:
    phase = [0, 0, 1, 1]
    ans = 0
    flag = False
    for i in range(0, n):
        temp = [a * (phase[0] + 1), b * (phase[1] + 1),
                a * (phase[2] + 1) * b * phase[3], a * phase[2] * b * (phase[3] + 1)]
        m = temp.index(min(temp))
        if not flag and temp[m] > a * b:
            ans = a * b
            flag = True
        else:
            if m == 0:
                phase[0] += 1
            elif m == 1:
                phase[1] += 1
            elif m == 2:
                phase[2] += 1
            elif m == 3:
                phase[2] += 1
            ans = temp[m]
    print(ans % (pow(10, 9) + 7))

