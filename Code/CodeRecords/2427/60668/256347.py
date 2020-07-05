def arrays_43_diff(list = []):
    list_0 = []
    for item in list:
        if item not in list_0:
            list_0.append(item)
    co = 0
    count = 0
    list_1 = []
    for item in list_0:
        co = 0
        for i in range(len(list)):
            if list[i]==item:
                co += 1
            if co >= 2:
                co = i
                for j in range(0,i):
                    if list[j]==list[i]:
                        list_1.append(j)
                        break
                break
    if len(list)==len(list_0):
        print(-1)
    else:
        print(list_1[0]+1)
if __name__=='__main__':
    for i in range(int(input())):
        n = input()
        list = [int(i) for i in input().split()]
        arrays_43_diff(list)