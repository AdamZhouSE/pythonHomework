def correct():
    if str_2[0] == '0':
        return int('1' + str_2[1:], 2)
    else:
        for i in range(1, len(str_2)):
            ch = '0' if str_2[i] == '1' else '1'
            lst_2.append(int(str_2[:i] + ch + str_2[i+1:], 2))
    if str_3[0] == '0':
        num = int('1' + str_3[1:], 3)
        return num if num in lst_2 else int('2' + str_3[1:], 3)
    else:
        choices = ['0', '1', '2']
        for i in range(len(str_3)):
            idx = 1 if i == 0 else 0
            for j in range(idx, len(choices)):
                if choices[j] != str_3[i]:
                    num = int(str_3[:i] + choices[j] + str_3[i + 1:], 3)
                    if num in lst_2:
                        return num


str_2, str_3 = input(), input()
lst_2, lst_3 = [], []
print(correct(), end='')
