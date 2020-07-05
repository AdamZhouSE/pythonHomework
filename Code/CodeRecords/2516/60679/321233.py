number = int(input())
list = []
out = []
for i in range(number):
    read = input().split(',')
    read = [int(read[j]) for j in range(len(read))]
    list.append(read)
for i in range(number):
    largest = list[i][len(list[i])-1]
    right = -1
    gap = -1
    for j in range(number):
        if(list[j][0]>=largest and (gap==-1 or list[j][0]-largest<gap)):
            gap = list[j][0]-largest
            right = j
    out.append(right)
print(out)