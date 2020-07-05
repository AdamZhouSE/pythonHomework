inp = eval(input())

def one_number(s):
    count = 0
    for i in s:
        if(i == '1'):
            count = count+1
    return count

for n in range(inp):
    i = eval(input())
    #print("输入: {}".format(i))
    j = bin(i)
   # print("二进制表示： {}".format(j))
    temp = 0
    re = one_number(j)
    #print("数量{}".format(re))
    if(re == 1):
        for i in j:
            temp =temp+1
            if(i == '1'):
                print(temp-1)
                break
    else:
        print("-1")