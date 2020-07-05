NumOfEg = int(input())
result = []
for i in range(NumOfEg):
    num = int(input())
    string = bin(num)[2:]
    while len(string) != 10:
        string = "0" + string
    res = ""
    for i in range(int(len(string)/2)):
        res = res+string[2*i:2*i+2][::-1]
    result.append(int(res, 2))
for i in result:
    print(i)