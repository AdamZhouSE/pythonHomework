import math
t = int(input())
opposition = ['North','East','South','West']
for i in range(t):
    n = int(input())
    lst = input().split(' ')
    face = 'North'
    x = 0
    y = 0
    for i in range(n):
        opp = lst[2*i]
        dis = int(lst[2*i+1])
        #定方向
        if opp == 'R':
            face = opposition[(opposition.index(face)+1)%4]
        elif opp == 'L':
            face = opposition[(opposition.index(face)+3)%4]
        elif opp == 'D':
            face = opposition[(opposition.index(face)+2)%4]
        
        if face == 'North':
            y+=dis
        elif face == 'South':
            y-=dis
        elif face == 'West':
            x-=dis
        elif face == 'East':
            x+=dis
    distance = math.floor(math.sqrt(x**2+y**2))
    print(distance,end = ' ')
    print(face[0])