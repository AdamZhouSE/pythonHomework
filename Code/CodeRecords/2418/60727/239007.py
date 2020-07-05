def s(tomato,cheese):
    flag = 0
    for i in range(0,cheese+1):
        if tomato==0 and cheese == 0:
            return('[0, 0]')
            flag=1
            break
        if i*4+(cheese-i)*2==tomato :
            return('[{}, {}]'.format(i,cheese-i))
            flag = 1
            break
        
    if flag == 0 :
        return('[]')
tomato = int(input())
cheese = int(input())
print(s(tomato,cheese))