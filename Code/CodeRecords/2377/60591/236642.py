def key(list):
    return list[0]

def isValid(list):
    list.sort(key = key)
    k = (list[1][1]-list[0][1])/(list[1][0]-list[0][0])
    for m in range(1,len(list)):
        temp = (list[m][1]-list[0][1])/(list[m][0]-list[0][0])
        if(temp!=k):
            return True
    return False

n = eval(input())
result = []
while(n!=0):
    n = n - 1
    temp = list(map(int,input().split(",")))
    result.append(temp)

if(isValid(result)):
    print("True")
else:
    print("False")