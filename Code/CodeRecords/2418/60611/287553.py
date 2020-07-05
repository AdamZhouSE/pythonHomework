tomato=int(input())
cheese=int(input())
if tomato>4*cheese or tomato<2*cheese or tomato%2==1:
    print("[]")
else:
    result=[]
    for i in range(tomato//4+1):
        if 4*i+(cheese-i)*2==tomato:
            result.append(i)
            result.append(cheese-i)
            print(result)
            break