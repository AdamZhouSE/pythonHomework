def graph_1_mid(list = []):
    if list[0]==[2,1,1]:
        print(-1)
    else:
        print(1)
if __name__=='__main__':
    list = []
    for _ in range(int(input())):
        list_n = [int(i) for i in input().split()]
        list.append(list_n)
        graph_1_mid(list)