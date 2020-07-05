def findWinner(list):
    dict = {}
    for name in list:
        if(name in dict):
            dict[name] += 1
        else:
            dict[name] = 1
    high = 0
    result = ""
    for name in dict.keys():
        if(dict[name] > high):
            high = dict[name]
            result = name
    print(result + " " + str(high))

n = eval(input())
while(n!=0):
    n -= 1
    input()
    findWinner(input().split(" "))