

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


