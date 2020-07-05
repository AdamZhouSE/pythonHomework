from fractions import Fraction

m = input()
i = 1
bound = len(m)
while i < bound:
    if m[i] == "-":
        m = m[: i] + "+" + m[i:]
        bound += 1
        i += 1
    i += 1
temp = [Fraction(x) for x in m.split("+")]
ans = temp[0]
for i in range(1, len(temp)):
    ans += temp[i]
print(str(ans.numerator) + "/" + str(ans.denominator))
