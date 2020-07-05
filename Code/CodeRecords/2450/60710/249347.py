#第一个和最后一个元素的位置

def solve(num,target):
    num=list(num)
    if num.count(target)==0:
        return [-1,-1]
    re=[]
    index1=num.index(target)
    re.append(index1)
    num.reverse()
    index2=num.index(target)
    re.append(len(num)-index2-1)
    return re

if __name__ == '__main__':
    num=eval(input())
    t=int(input())
    print(solve(num,t))