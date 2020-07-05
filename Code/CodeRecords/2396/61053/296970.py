def minLst(numlst,n):
    #将原始的排位也记录下来
    newlst = []
    for i in range(n):
        temp = [numlst[i],i]
        newlst.append(temp)

    index = 0
    res = []
    while index < n:
        minval = newlst[index][0]
        minindex = index
        #找到最小值
        for i in range(index,len(numlst)):
            if (newlst[i][0]<newlst[minindex][0]) or (newlst[i][0]==newlst[minindex][0] and newlst[i][1]<newlst[minindex][1]):
                minval = newlst[i][0]
                minindex = i
        #将minindex加到list中
        res.append(minindex+1)
        #排序完成
        if minindex == index:
            break
        #进行翻转，从index到minindex进行翻转
        for i in range(int((minindex-index+1)/2)):
            temp1 = newlst[index+i][0]
            temp2 = newlst[index+i][1]

            newlst[index+i][0] = newlst[minindex-i][0]
            newlst[index + i][1] = newlst[minindex - i][1]

            newlst[minindex-i][0] = temp1
            newlst[minindex-i][1] = temp2
            
        index += 1
    return res

if __name__ == "__main__":
    n = int(input())
    numlst = list(map(int,input().split(" ")))
    res = minLst(numlst,n)
    for no in res:
        print(no,end=" ")