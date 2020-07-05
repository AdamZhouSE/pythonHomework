def fill(a, b, x1, x2) -> str:
    result = ""
    if (0 <= a <= 9 and b > 9) or (0 <= b <= 9 and a > 9):
        return "-"
    elif b - a == 1:
        return ""
    elif a - b >= 0:
        return "-"
    elif 0 <= a <= 9 and 0 <= b <= 9:
        if x1 == 3:
            for i in range(0, b - a - 1):
                result += "*"*x2
            return result
        else:
            for i in range(1, b - a):
                result += str(a+i) * x2
            return result
    else:
        if x1 == 3:
            for i in range(0, b - a - 1):
                result += "*"*x2
            return result
        else:
            for i in range(1, b - a):
                result += chr(a + i) * x2
            if x1 == 2:
                result = result.upper()
            return result


p = list(map(int, input().split()))
p1, p2, p3 = p[0], p[1], p[2]
ls = list(input().split("-"))
ls2 = []
final = ""
for j in range(1, len(ls)):
    temp = fill(ord(ls[j - 1][-1]), ord(ls[j][0]), p1, p2)
    if p3 == 2:
        temp = reversed(temp)
    ls2.append(temp)
ls2.append("")
for j in range(0, len(ls)):
    final = final + ls[j] + ls2[j]
print(final)