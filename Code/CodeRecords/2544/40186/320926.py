t = int(input())
for i in range(t):
    temp1 = input().split()
    temp2 = input().split()
    if (int(temp1[2])-int(temp1[0]))*(int(temp2[3])-int(temp2[1]))==(int(temp2[2])-int(temp2[0]))*(int(temp1[3])-int(temp1[1])):
        print(1)
    else:
        print(0)