t = int(input())
for index in range(t):
    len = int(input())
    numbers = input()
    d = int(input())
    result = numbers[d*2:]+" "+numbers[:d*2]
    print(result.strip()+"\n")