def func(n, m : str) -> list :
    list = []
    min = 2000000.0
    rem = []
    answer = []
    for i in range(len(n)):
        for j in range(i+1, len(n)) :
            list.append([n[i], n[j]])
    for x in range(int(m)):
        for i in range(len(list)):
            tmp = (int(list[i][0]) / int(list[i][1]))
            if min > tmp:
                min = tmp
                rem = list[i]
        answer = rem
        list.remove(rem)
        min = 2000000.0
    return answer



n = input().replace("[","").replace("]","").replace(" ","").split(",")
m = input()
print(func(n,m))
    