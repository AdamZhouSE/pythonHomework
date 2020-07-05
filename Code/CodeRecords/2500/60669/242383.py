
def specialReverse(num,list):
    result.append(num)
    temp=list[0:num]
    temp.reverse()
    return temp+list[num:]

def findMaxIndex(num,list):     # num是前几个数
    temp=list[0:num]
    biggest=max(temp)
    return list.index(biggest)    # 注意这里是index
def whetherSorted(num,list):
    temp=list[0:num]
    normal=sorted(temp)
    if temp==normal:
        return True
    else:
        return False

if __name__ == '__main__':
    result = []
    import math
    list=eval(input())
    size=len(list)

    for i in range( 0, (size-1)*2) :
        x=math.floor(i/2)
        if whetherSorted(size-x,list):
            break
        else:
            index=findMaxIndex(size-x,list)
            if index==0:
                list=specialReverse(size-x,list)
            else:
                list=specialReverse(index+1,list)

    print(result)

