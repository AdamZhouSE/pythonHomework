def solve():
    nums = list(map(int, input()[1:-1].split(',')))
    dict={}
    for num in nums:
        dict[num]=0
        i=1
    while True:
        if dict.get(i)==None:
            break
        i+=1
    print(i)
if  __name__ == '__main__' :
    solve()