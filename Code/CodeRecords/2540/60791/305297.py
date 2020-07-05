def able(cin,car):
    global c
    
    for j in range(cin[2]+1):
        for i in range(cin[0],cin[1]):
            if i >len(car)-1:
                break
            if car[i] + j > c:
                return j-1
    return cin[2]

def do(cin,car,num):
    for i in range(cin[0],cin[1]):
        car[i] += num
    return car
k,n,c = [int(i) for i in input().split(' ')]
cin = []
for i in range(k):
    temp = [int(i) for i in input().split(' ')]
    cin.append(temp)

cin.sort(key = lambda x:(x[1],-x[0]))

car = [0]*(n+n)
res = 0
for i in range(len(cin)):
    num = able(cin[i],car)
    car = do(cin[i],car,num)
    res += num
print(res)

