def find(string):
    strings = string.split(" ")
    temp = []
    for before in strings:
        before = list(before.lower())
        before.sort()
        temp.append(''.join(before))
    dict = {}
    for before in temp:
        if before in dict:
            dict[before] += 1
        else:
            dict[before] = 1
    result = list(map(int,dict.values()))
    result.sort()
    result = list(map(str,result))
    return " ".join(result)

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    print(find(input()))