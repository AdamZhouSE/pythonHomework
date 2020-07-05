single_dict = {'0':'', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}
ten_dict = {'0':'', '2':'Twenty', '3':'Thirty', '4':'Forty', '5':'Fifty', '6':'Sixty', '7':'Seventy', '8':'Eighty', '9':'Ninety'}
ten_special_dict = {'10':'Ten', '11':'Eleven', '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', '16':'Sixteen', '17':'Seventeen', '18':'Eighteen', '19':'Nineteen'}
num = input()
num = str(num)
control = 0
for i in range(len(num)):
    if control == 1:
        control = 0
        continue
    bitPos = len(num) - i
    if bitPos == 1:
        print(single_dict[num[i]])
    elif bitPos == 2:
        if num[i] == '1':
            temp_str = num[i:(i + 2)]
            print(ten_special_dict[temp_str], end = ' ')
            control = 1
        else:
            print(ten_dict[num[i]], end = ' ')
    elif bitPos == 3 or bitPos == 6 or bitPos == 9:
        if num[i] == '0':
            pass
        else:
            print(single_dict[num[i]] + ' ' + 'Hundred', end = ' ')
    elif bitPos == 4:
        if num[i] == '0':
            print('Thousand', end = ' ')
        else:
            print(single_dict[num[i]] + ' ' + 'Thousand', end = ' ')
    elif bitPos == 5:
        if num[i] == '1':
            temp_str = num[i:(i + 2)]
            print(ten_special_dict[temp_str] + ' ' + 'Thousand', end = ' ')
            control = 1
        else:
            print(ten_dict[num[i]], end = ' ')
    elif bitPos == 7:
        if num[i] == '0':
            print('Million', end = ' ')
        else:
            print(single_dict[num[i]] + ' ' + 'Million', end = ' ')
    elif bitPos == 8:
        if num[i] == '1':
            temp_str = num[i:(i + 2)]
            print(ten_special_dict[temp_str] + ' ' + 'Million', end = ' ')
            control = 1
        else:
            print(ten_dict[num[i]], end = ' ')
    elif bitPos == 10:
        print(single_dict[num[i]] + ' ' + 'Billion', end = ' ')