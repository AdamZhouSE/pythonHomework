def greyCode(n):#n位的格雷码
    pre_level=["0","1"]#上一层的格雷码  初始值是一位的格雷码
    bits=1
    while bits<n:
        level=["0"+x for x in pre_level]
        level_mirror=["1"+x for x in reversed(pre_level)]
        pre_level=level+level_mirror
        bits+=1
    return pre_level


def solution(n,start):
    greyCodes=greyCode(n)
    ind=0
    for code in greyCodes:
        integ=int(code,2)
        if integ==start:
            ind=greyCodes.index(code)
            break
    temp=greyCodes*2
    lst=temp[ind:ind+2**n]
    nums=[]
    for code in lst:
        nums.append(int(code,2))
    return nums


if __name__=="__main__":
    n=int(input())
    start=int(input())
    ans=solution(n,start)
    print(ans)