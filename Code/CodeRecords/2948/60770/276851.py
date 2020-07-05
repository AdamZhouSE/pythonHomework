def solve():
    src=input()
    base=int(input())
    nums=transfer(src,base)
    while True:
        if len(nums)<=2 or int(nums)==100:
            break
        nums=proc(nums)
    print(int(nums),end='')

def transfer(src,base):
    res=""
    for i in range(len(src)):
        cur=ord(src[i])-ord('A')+base
        res+=str(cur)
    return res

def proc(src):
    res=''
    for i in range(len(src)-1):
        res+=(str(int(src[i])+int(src[i+1]))[::-1])[0]
    return res

if __name__ == '__main__':
    solve()