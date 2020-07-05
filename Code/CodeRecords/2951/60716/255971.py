def caculate_2(temp):
    temp.reverse()
    index=0
    for i in range(len(temp)):
        index = index + temp[i]*(2**i)
    return index

def caculate_3(temp):
    temp.reverse()
    index=0
    for i in range(len(temp)):
        index = index + temp[i]*(3**i)
    return index

sec = input()
third = input()
a1 = list(sec)
b1 = list(third)
a = [int(i) for i in a1]
b = [int(i) for i in b1]
k = [0,1,2]
answera = list()
answerb = list()
answer = list()
for i in range(len(a)):
    temp = a.copy()
    temp[i] = 1-temp[i]
    caculate_2(temp)
for i in range(len(b)):
    temp = b.copy()
    k1 = k.copy()
    k1.pop(temp[i])
    for j in range(2):
        temp[i] = k1[j]
        caculate_3(temp)
for i in range(len(answera)):
    temp = answera[i]
    for j in range(len(answerb)):
        if temp==answerb[i]:
            answer.append(temp)
print(answer[0])
