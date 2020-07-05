string = input()
num = int(input())
strings =[]
temp = ""
for i in range(len(string)):
    if string[i] == 'B':
        temp = temp[:-1]
    elif string[i] == 'P':
        strings.append(temp)
    else:
        temp += string[i]
# print(strings)


def cal(str1, str2):
    # print(str1,str2)
    count = 0
    ct = True
    if len(str1)>len(str2):
        return count
    else:
        for j in range(len(str2)):
            if str2[j] == str1[0]:
                for k in range (len(str1)):
                    if not str1[k] == str2[k+j]:
                        ct = False
                        break
                if ct:
                    count += 1
                    j += len(str1)
                ct = True
        return count


for i in range(num):
    op = list(map(int, input().split(" ")))
    # print(op)
    print(cal(strings[op[0]-1],strings[op[1]-1]))

#
# aPaPBbP
# 3
# 3 4
# 1 3
# 2 3
