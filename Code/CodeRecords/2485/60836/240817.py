'''
给定一个单词数组，按排序顺序（计数的递增顺序）一起打印所有字符相同组的计数
例如，如果给定的数组是{“ cat”，“ dog”，“ tac”，“ god”，“ act”}
则分组的字谜是“（dog，god）（cat，tac，act）”
因此输出为2 3
'''


def is_equal(a,b):
    a=list(a)
    b=list(b)
    if len(a)!=len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] not in b:
                return False
        for i in range(len(b)):
            if b[i] not in a:
                return False
    return True

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    N = int(string_list[i])
    str_list=string_list[i+1].split(" ")

    result=[]
    while len(str_list)>0:
        m=1
        number = 1
        while m<len(str_list):
            if is_equal(str_list[m],str_list[0]):
                number=number+1
                del str_list[m]
            else:
                m=m+1
        result.append(number)
        del str_list[0]

    result.sort()
    print(" ".join(str(m) for m in result))

    i=i+2


