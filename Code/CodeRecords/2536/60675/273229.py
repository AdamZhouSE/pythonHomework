def func(l: list) -> list :
    list ,tmp ,target ,answer = l, "", "JFK", ["JFK"]
    while len(list) > 0:
        for i in range(len(list)):
            if list[i][0] == target :
                target = list[i][1]
                answer.append(target)
                list.remove(list[i])
                break
    return answer
n = "l = " + input()
exec(n)
print(func(l))