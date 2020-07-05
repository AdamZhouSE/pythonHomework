if __name__=='__main__':
    line = input().split(' ')
    m = int(line[0])
    q = int(line[1])

    nums = list(map(int,input().split(' ')))
    nums.sort(reverse=True)

    for i in range(q):
        order = list(map(int,input().split(' ')))
        if order[0]==1:
            print(nums[order[1]-1])
        else:
            nums.append(order[1])
            nums.sort(reverse=True)