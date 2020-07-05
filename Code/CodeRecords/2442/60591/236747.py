string = input().split("[")[1]
string = string.split("]")[0]
temp = list(map(int,string.split(",")))
temp.sort()
result = 0
for x in range(1,len(temp)):
    if(temp[x]-temp[x-1] > result):
        result = temp[x] - temp[x-1]
print(result)