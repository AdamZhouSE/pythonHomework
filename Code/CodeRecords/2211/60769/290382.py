if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    people = []
    for i in range(n):
        pre,index = input().split()
        index = int(index)
        if index == 0:
            people.append(pre)
        else:
            people.append(pre + people[index-1])
    for i in range(k):
        pre = input()
        count = 0
        for item in people:
            if item.startswith(pre):
                count+=1
        print(count)