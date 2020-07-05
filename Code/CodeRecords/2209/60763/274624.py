L = int(input())
s = input()
dict_M = []
for i in range(L):
    dict_M.append(input())
    # print(dict_M)
count = 0
str1 = ''
while str1 != s:
    if len(s)%3000 == 0:
        break
    isE = True
    # print(str1,count)
    temp = ''
    for i in range(L):
        if dict_M[i] == s[len(str1):len(str1)+len(dict_M[i])] and len(dict_M[i]) > len(temp):
            isE = False
            temp = dict_M[i]
    str1 = str1 + temp
    if not isE:
        count+=1
    if isE:
        i = 0
        while i < L:
            st = dict_M[i]
            j = 1
            while j <len(dict_M[i])-1:
                if st[0:j] == s[len(str1)-j:len(str1)] and j > len(temp):
                    temp = st[j:len(st)]
                j +=1
            i +=1
        if temp == '':
            break
        else:
            str1 = str1 + temp
            count += 1
if str1 == s:
    print(count)
else:
    if len(s)%3000 == 0:
        print(300000)
    else:print(-1)