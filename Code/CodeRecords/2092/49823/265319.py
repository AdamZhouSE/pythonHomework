def an(n,nums):
    l=list()
    for i in range(n):
        l.append(set())
    r=1
    while True:
        for i in range(n):
            l[nums[i]].add(i+1)
            for j in l[i]:
                l[nums[i]].add(j)
            if nums[i]+1 in l[nums[i]]:
                print(r)
                return
            else:
                r+=1
if __name__ == '__main__':
    an(int(input()),[int(i) for i in input().split(' ')])
