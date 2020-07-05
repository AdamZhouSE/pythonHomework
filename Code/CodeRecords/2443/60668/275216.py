def maxNum(list=[]):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if str(list[j])+str(list[j+1])>str(list[j+1])+str(list[j]):
                list[j],list[j+1]=list[j+1],list[j]
    s = ''
    if list[-1] == 0:
        print(0)
    for i in list:
        s = str(i) +s
    print(s)
if __name__=='__main__':
    list = eval(input())
    maxNum(list)