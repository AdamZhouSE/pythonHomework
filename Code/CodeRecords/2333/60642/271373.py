import math

base1 = int(input())
base2 = int(input())
bound = int(input())
out = []
for i in range(int(math.log(bound,base1))+1):
    for j in range(int(math.log(bound, base2)) + 1):
        temp = pow(base1,i)+pow(base2,j)
        if(temp<=bound):
            if(out.count(temp)==0):
                out.append(temp)
        else:
            break
out.sort()
print(out)