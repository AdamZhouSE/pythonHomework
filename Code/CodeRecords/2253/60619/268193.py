inp = input().strip().split(" ")
length = int(inp[0])
t = int(inp[1])
numbers = [int(i) for i in input().strip().split(" ")]
for i in range(t):
    li = input().strip().split(" ")
    instruction = int(li[0])
    if instruction == 3:
        pos = int(li[1]) - 1
        numbers[pos] = int(li[2])
    else:
        l = int(li[1])-1
        r = int(li[2])-1
        x = int(li[3])
        newl = numbers[l:r+1]
        newl.sort()
        if instruction == 1:
            print(newl.index(x)+1)
        elif instruction == 2:
            print(newl[x-1])
        elif instruction == 4:
            for j in range(len(newl)):
                if newl[j] >= x:
                    print(newl[j-1])
                    break
                elif j == len(newl)-1:
                    print(newl[j])
        elif instruction == 5:
            for j in range(len(newl)):
                if newl[j] > x:
                    print(newl[j])
                    break
