questNum = int(input())

for quest in range(questNum):
    numerator = int(input())
    denominator = int(input())
    answer = []
    res = []
    quotient = []
    resNum = 0
    flag = False
    if numerator % denominator == 0:
        print(str(numerator // denominator), end="")
    else:
        answer.append(str(numerator // denominator))
        answer.append('.')
        if numerator // denominator > 0:
            numerator -= (numerator // denominator) * denominator

        while True:
            res.append(str(numerator))
            while numerator < denominator:
                numerator *= 10

            resNum = numerator % denominator
            quotient.append(str(numerator // denominator))
            if resNum == 0:
                break
            numerator -= (numerator // denominator) * denominator
            res.append(str(res))
            if str(resNum) in res:
                flag = True
                break

        if flag:
            answer.append("(")
            for q in quotient:
                answer.append(str(q))
            answer.append(")")
        else:
            for q in quotient:
                answer.append(str(q))
    s = ""
    for a in answer:
        s += a
    print(s)