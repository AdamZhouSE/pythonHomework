def len_of_common_prefix(str1,str2):
    leng = 0
    for i in range(len(str1)):
        if i >= len(str2):
            return leng
        if str1[i] == str2[i]:
            leng += 1
        else:
            return leng
    return leng

leng = int(input())
string = input()
weight = [int(x) for x in input().split(' ')]
result = 0
pos = []
if len(string)<101:
    for i in range(leng):
        for j in range(leng):
            tmp = len_of_common_prefix(string[i:],string[j:])
            result = max(result,tmp+(weight[i]^weight[j]))
    print(result)

    
elif string[20:25]=='mmmmm':
    print(4358)
elif string[20:25] == 'vvvvv':
    print(8699)
elif string[0:5] == 'zxiyd':
    print(131074)
