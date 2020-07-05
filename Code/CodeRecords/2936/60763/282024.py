def numToint(s):
    dict_N = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5
        ,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'R':7,'S':7,'T':8,'U':8,'V':8,
              'W':9,'X':9,'Y':9}
    num = "0123456789"
    t = ''
    for i in range(len(s)):
        temp = str(s[i])
        if temp in num:
            t+=temp
        else:
            t += str(dict_N[s[i]])
    return t


N = int(input())
number = []
# index = [""]*N
for i in range(N):
    s = list(input())
    temp = -1
    # for j in range(s.count('-')):
    #     index[i] += str(s.index('-',temp+1))
    #     temp = s.index('-',temp+1)
    # print(index)
    for j in range(s.count('-')):
        s.remove('-')
    # print(s,''.join(s))
    number.append(numToint(''.join(s)))
num = []
sum1 = []
index = [""]*N
for i in range(len(number)):
    # print(number[i])
    if number.count(number[i]) >1 and not number[i] in num:
        num.append(number[i])
        sum1.append(number.count(number[i]))
    i+=1
# for i in range(N):
#     for j in range(len(index[i])):
#         number[i] = number[0:int(index[i][j])] + '-' + number[int(int(index[i][j])):len(number[i])]
if len(num) == 0:
    print("No duplicates.",end='')
else:
    for j in range(len(num)):
        print(num[j][0:3]+'-'+num[j][3:len(num[j])], end=' ')
        print(sum1[j])