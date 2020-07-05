NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = input().split(" ")
    result.append(pow(2,int(num[1]))-int(num[0]))
for i in result:
    print(i)