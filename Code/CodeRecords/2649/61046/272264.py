num = input()

lst =[]
for i in range(int(num)):
    lst.append(input())

for i in range(len(lst)):
    temp = lst[i].split(' ')
    n = int(temp[0])
    l = int(temp[1])
    r = int(temp[2])
    res = ''
    binary = list(bin(n))
    del binary[0:2]
    binary =list(map(int,binary))

    for j in range(len(binary)-r,len(binary)-l+1):
        if binary[j] == 0:
            binary[j] = 1
        else:
            binary[j] = 0
    res = ''.join(list(map(str,binary)))
    res = '0b'+res
    print(int(res,2))