NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = input().split(" ")
    result.append("-"+str(int(num[0])-int(num[1])+1))
for i in result:
    print(i)