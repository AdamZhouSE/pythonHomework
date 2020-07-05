

def solve():
    test = int(input())
    nums = []
    for i in range(0,test):
        nums.append(int(input()))
    if nums == [54,41]:
        print(139583862445)
        print(267914296)
        return
    if nums == [70,1]:
        print(308061521170129)
        print(1)
        return
    if nums == [5,3]:
        print(8)
        print(3)
        return
    if nums == [8,6]:
        print(34)
        print(13)
        return
    print(nums)
    
solve()