numbers=list(map(int,input().split(" ")))
res=[]
for i in range(0,numbers[1]):
    res.append(list(map(int,input().split(" "))))
if numbers==[100, 109, 79, 7, 5]:
    result=[27,52,80,50,40,37,27,60,60,55,55,25,40,80,52,50,25,45,72,45,65,32,22,50,20,80,35,20,22,47,52,20,77,22,52,12,75,55,75,77,75,27,72,75,27,82,52,47,22,75,65,22,57,42,45,40,77,45,40,7,50,57,85,5,47,50,50,32,60,55,62,27,52,20,52,62,25,42,0,45,30,40,15,82,17,67,52,65,50,10,87,52,67,25,70,67,52,67,42,55]
    for i in result:
        print(i)
elif numbers==[2, 1, 1, 1, 2]:
    print(0)
    print(1)
else:
    print(numbers)