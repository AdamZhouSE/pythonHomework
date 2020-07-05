def single(single):
    """
    将一个数字翻译成英文(非十位)
    :param single: 一个数字，字符串格式
    :return: 对应英语
    """
    dict = {
        '0' : 'Zero',  '1' : 'One',    '2' : 'Two',
        '3' : 'Three', '4' : 'Four',   '5' : 'Five',
        '6' : 'Six',   '7' : 'Seven',  '8' : 'Eight',  '9' : 'Nine'
    }
    return dict[single]

def double(double):
    """
    十位和个位 的 对应英文
    :param double: 字符串,必为两位数，不足的在调用者中补零
    :return: 对应英文
    """
    dict = {
        '10':'Ten' ,     '11':'Eleven' ,   '12':'Twelve',
        '13':'Thirteen', '14':'Fourteen',  '15':'Fifteen',
        '16':'Sixteen',  '17':'Seventeen', '18':'Eighteen',
        '19':'Nineteen',
        '20':'Twenty',   '30':'Thirty',    '40':'Forty',
        '50':'Fifty',    '60':'Sixty',     '70':'Seventy',
        '80':'Eighty',   '90':'Ninety'
    }
    if (double[0] == '1') or (double[0] != '0' and double[1] == '0'):
        return dict[double]
    elif (double[0] == '0') and (double[1] != '0'):
        return single(double[1])
    elif (double[0] == '0') and (double[1] == '0'):
        return ''
    else:
        return dict[double[0]+'0']+' '+single(double[1])

def three(str):
    """
    得出英文
    :param str: '三位数'的字符串，不足三位的在调用者中补零
    :return: 对应英文
    """
    English = ''
    if str[0] != '0':
        English += (single(str[0]) + ' Hundred ')
    English += double(str[1:3])
    return English

num = input()
num = '0'*((len(num)+2)//3*3 - len(num)) + num
list = [num[i:i+3] for i in range(0,len(num),3)]
result = three(list[-1])
if len(list)>=2:
    result = three(list[-2]) + ' Thousand ' + result
if len(list)>=3:
    result = three(list[-3]) + ' Million ' + result
if len(list)>=4:
    result = three(list[-4]) + ' Billion ' + result

print(result)