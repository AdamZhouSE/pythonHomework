res=1

def solve():
    global res
    total=int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        find(num,1,nums)
    print(res)

def find(current,counter,nums=[]):
    global res
    newli=list(filter(lambda x:x>current and x<=current*2,nums))
    for num in newli:
        current=num
        if counter+1>res:
            res=counter+1
        find(current,counter+1,nums)

if  __name__ == '__main__' :
    solve()