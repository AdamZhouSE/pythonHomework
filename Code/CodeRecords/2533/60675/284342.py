def func(l: list) -> list:
    even, odd, answer = [], [], []
    for i in l :
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for i in even :
        answer.append(i)
    for i in odd:
        answer.append(i)
    return answer



n = "l =" + input()
exec(n)
print(func(l))