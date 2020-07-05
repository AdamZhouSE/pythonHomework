num = int(input())
give = [int(i) for i in input().split()]
receive = []
for m in range(len(give)):
    receive.append(0)
for index in range(len(give)):
    receive[give[index]-1] = index+1
result = receive
for i in range(len(result)):
    if(i != len(result)-1):
        print(result[i],end=" ")
    else:
        print(result[i])