def test():
    string = list(input())
    sort_str = [0] * len(string)
    copy_string = list(string)
    copy_string.sort()
    copy_string[0] = [copy_string[0], 1]
    count = 1
    for i in range(1, len(copy_string)):
        if copy_string[i] != copy_string[i - 1][0]:
            count = count + 1
            copy_string[i] = [copy_string[i], count]
        else:
            copy_string[i] = [copy_string[i], count]
    for i in range(0, len(string)):
        for j in copy_string:
            if j[0] == string[i]:
                sort_str[i] = j[1]
                break
    base = 1
    while len(set(sort_str)) != len(sort_str):
        sort_str = list(map(str, sort_str))
        for i in range(0, len(sort_str) - base):
            sort_str[i] = sort_str[i] + sort_str[i + base]
        for i in range(len(sort_str) - base, len(sort_str)):
            sort_str[i] = sort_str[i] + '0'
        sort_str = list(map(int, sort_str))
        copy_sort_str = list(sort_str)
        copy_sort_str.sort()
        copy_sort_str[0] = [copy_sort_str[0], 1]
        count = 1
        for i in range(1, len(copy_sort_str)):
            if copy_sort_str[i] != copy_sort_str[i - 1][0]:
                count = count + 1
                copy_sort_str[i] = [copy_sort_str[i], count]
            else:
                copy_sort_str[i] = [copy_sort_str[i], count]
        new_sort_str = [0] * len(sort_str)
        for i in range(0, len(copy_sort_str)):
            for j in copy_sort_str:
                if j[0] == sort_str[i]:
                    new_sort_str[i] = j[1]
                    break
        sort_str = new_sort_str
        base=base*2
    res=[]
    for i in range(0,len(sort_str)):
        res.append(sort_str.index(i+1)+1)
    res = ' '.join(list(map(str, res)))
    print(res)


test()
