def caculate_2(temps):
    print(temps,end=' ')
    y = temps.copy()
    y.reverse()
    index=0
    for x in range(len(y)):
        index = index + y[x]*(2**x)
    print(index)
    answera.append(index)

def caculate_3(temps):
    print(temps,end=' ')
    y = temps.copy()
    y.reverse()
    index=0
    for x in range(len(y)):
        index = index + y[x]*(3**x)
    print(index)
    answerb.append(index)

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
    print("2进制-{}change:".format(i))
    temp = a.copy()
    temp[i] = 1-temp[i]
    caculate_2(temp)
for i in range(len(b)):
    print("3进制-{}change:".format(i))
    temp = b.copy()
    k1 = k.copy()
    k1.pop(temp[i])
    print(k1)
    for j in range(2):
        temp[i] = k1[j]
#        print(temp)
        caculate_3(temp)
for i in range(len(answera)):
    temp = answera[i]
    for j in range(len(answerb)):
        if temp==answerb[i]:
            answer.append(temp)
print(answera[0],end='')

