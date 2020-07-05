if __name__ == '__main__':
    lst = []
    n = int(input())
    for i in range(n):
        op, val = map(int,input().split(" "))
        if op == 1:
            index = 0
            while index < len(lst):
                if lst[index] > val:
                    break
                index += 1
            lst.insert(index,val)
        elif op == 2:
            index = lst.index(val)
            del lst[index]
        elif op == 3:
            print(lst.index(val)+1)
        elif op == 4:
            print(lst[val-1])
        elif op == 5:
            index = 0
            while index < len(lst) and lst[index] < val:
                index+=1
            print(lst[index-1])
        elif op == 6:
            index = 0
            while index < len(lst) and lst[index] <= val:
                index += 1
            print(lst[index])