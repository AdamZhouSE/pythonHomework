def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        numList = [n]    #存放所有计算出来的数，用于判断是否存在环
        while n!=1:     #如该计算结果为1，说明该数是快乐的数
            sum=0
            for i in str(n):
                sum += int(i)**2
            if sum not in numList:     #判断是否存在环
                numList.append(sum)
            else:       #存在环就说明该数不是快乐的数
                return False
            n = sum
        return True
    
n=int(input())
if isHappy(n):
    print(True)
else:
    print(False)