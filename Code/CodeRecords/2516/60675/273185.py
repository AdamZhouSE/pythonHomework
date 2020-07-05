def func(l : list) -> list:
    min , li , min_index= 20000 , [], 0
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                if l[i][1] <= l[j][0] and l[j][0] < min:
                    min = l[j][0]
                    min_index = j
        if min == 20000 and min_index == 0:
            li.append(-1)
        else:
            li.append(min_index)
            min = 20000
            min_index = 0
    return li

num = int(input())
l, tmp = [], []
for i in range(num):
    string = "tmp = [" + input() + "]"
    exec(string)
    l.append(tmp)
print(func(l))