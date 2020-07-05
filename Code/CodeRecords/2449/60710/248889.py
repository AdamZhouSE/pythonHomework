def solve(num,target):
    #num=list(map(int,num))
    if num.count(target)==0:
        return -1
    index=num.index(target)
    return index
    #front=[]  #用来存放前一个数组
    #after=[]  #用来存放后一个数组
if __name__ == '__main__':
    num=eval(input())
    target=int(input())
    print(solve(num,target))