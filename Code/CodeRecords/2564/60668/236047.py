def arrays3(k,x,list=[]):
    k = int(k)
    x = int(x)
    count = k-1
    count_1 = int(count/2)
    count_2 = count%2
    loc = list.index(x)
    begin = loc - count_1
    end = loc + count_1
    if count_2!=0:
        begin = begin-1
    list_re = []
    for i in range(begin,end+1):
        list_re.append(list[i])
    print(list_re)
if __name__ == '__main__':
    list = eval(input())
    k = input()
    x = input()
    arrays3(k,x,list)