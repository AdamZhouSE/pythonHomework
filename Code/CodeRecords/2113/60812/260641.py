table1 = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
          '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
table2 = {'11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen',
          '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}
table3 = {'1': 'Ten', '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty',
          '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
table4 = {0: '\n', 3: ' Thousand', 6: ' Million', 9: ' Billion'}


def myprint(s, t=''):
    global table1, table2, table3
    n = len(s)
    if n == 3:
        print('{} Hundred '.format(table1[s[0]]), end='')
        myprint(s[1:], t)
    elif n == 2:
        if s in table2.keys():
            print(table2[s]+t, end='')
        elif s[1] != '0':
            print(table3[s[0]], table1[s[1]]+t, end='')
        else:
            print(table3[s[0]]+t, end='')
    elif n == 1:
        print(table1[s]+t, end='')


s = input()
n = len(s)
ready = False
for i in range(9, -1, -3):
    if n > i:
        temp = s[:n - i]
        if temp.lstrip('0') != '':
            if ready:
                print(' ', end='')
            myprint(temp.lstrip('0'), table4[i])
            ready = True
        s = s[n - i:]
        n -= len(temp)