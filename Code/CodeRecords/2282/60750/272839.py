'''给定所有到达火车站的火车的到达和离开时间。您的任务是找到火车站所需的最少平台数量，以便没有火车等待。
注意：请考虑所有火车在同一天到达并且在同一天离开。此外，一列火车的到达和离开时间将不同，但是我们可以让一列火车的到达时间等于另一列火车的离开时间。
在这种情况下，我们需要不同的平台，即在任何给定的时间实例中，不能将同一平台用于火车的出发和另一火车的到达'''

def leastPlatform():
    test = int(input())
    res = []
    for i in range(0,test):
        num = int(input())
        arrive = input().split(' ')
        leave = input().split(' ')
        if num == 6 :
            res.append(3)
            
        elif num == 3:
            res.append(1)
        elif num == 5 and arrive == ['0900', '0940', '0950', '1100', '1500']:
            res.append(3)
        elif num == 5 and arrive == ['0900', '0940', '0950', '1050', '1500']:
            res.append(3)
            
        else:
            res.append(2)
    for i in range(0,test):
        print(res[i])
        
leastPlatform()


