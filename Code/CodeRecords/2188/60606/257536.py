line1 = input().split(" ")
n = int(line1[0])
k = int(line1[1])
stringA = input()
stringB = input()
time = int(input())
result = []
for i in range(time):
    line2 = input().split(" ")
    startA = int(line2[0])
    endA = int(line2[1])
    startB = int(line2[2])
    endB = int(line2[3])
    t = stringA[startA-1:endA]
    p = stringB[startB-1:endB]
    sum = 0
    if t.find(p) != -1:
        temp2 = t
        while(temp2.find(p) != -1):
            index = temp2.find(p)+startA
            sum += k-index
            temp2 = temp2.replace(p,"0"*len(p),1)
    result.append(sum)
for i in range(len(result)):
    print(result[i])
