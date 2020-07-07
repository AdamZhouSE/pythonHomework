def solve():
    string = input()
    max_letters = int(input())
    min_size = int(input())
    max_size = int(input())
    res = []
    for i in range(0,len(string) - min_size):
        tmp = ''
        tmp_str = ''
        for j in range(0,min_size):
            if string[i + j] not in tmp_str:
                tmp_str += string[i + j]
        if len(tmp_str) > max_letters:
             continue
        else:
            tmp = string[i:i + min_size]
        count = 1
        for j in range(i + 1,len(string) - min_size + 1):
            if string[j:j + min_size] == tmp:
                count+=1
        res.append(count)
    res.sort()
    if res == []:
        print(0)
        return
    print(res[len(res) - 1])


solve()
