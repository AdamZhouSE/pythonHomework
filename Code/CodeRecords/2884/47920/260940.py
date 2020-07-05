inp = input().split(" ")
num = int(inp[0])
d = int(inp[1])
#print(inp)

inp1 = input().split(" ")
#print(inp1)
count = 0
for i in range(num):
    for j in range(num):
        if(i != j):
            if(abs((int(inp1[i])-int(inp1[j]))) <= d):
                #print("{0},{1}".format(inp1[i],inp1[j]))
                count = count +1
print(count)
count = 0