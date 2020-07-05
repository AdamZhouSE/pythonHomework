def solve():
    input()
    nums = list(map(lambda x:x%3,map(int, input().split())))
    numOfzero=nums.count(0)
    numOfone=nums.count(1)
    numOftwo=nums.count(2)
    if numOftwo>=numOfone:
        numOftwo-=numOfone
        numOfzero+=numOfone
        numOfzero+=int(numOftwo/3)
        print(numOfzero)
        return
    else:
        numOfzero+=numOftwo
        numOfone-=numOftwo
        numOfzero+=int(numOfone/3)
        print(numOfzero)
        return

if  __name__ == '__main__' :
    total=int(input())
    for i in range(total):
        solve()