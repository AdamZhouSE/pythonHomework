string = input()
A = string[1:-1:1].split(",")
B = []
for C in A:
    B.append(int(C))
B.sort()
#print(B)
count = 1
index = 0
while index < len(B):
    if B[index] < count:
        index = index + 1
    elif B[index] == count:
        index = index + 1
        count = count + 1
    else:
        if B[index] == count:
            index = index + 1
            count = count + 1
        else:
            print(count)
            break
if index == len(B):
    print(count+1)
