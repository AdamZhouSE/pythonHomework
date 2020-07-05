num = int(input())
index = 0
for i in range(1,num+1):
    for j in range(1,num+1):
        if (i+j)*(i-j+1)//2==num:
#            print("{} {}".format(i,j))
            index+=1
print(index)