k = int(input())
def fun(list1):
    max = 1
    for i in range(0, len(list1)-1):
        if(list1[i+1]>=max+1):
            max=max+1
        else:
            break
    return max


for i in range(0, k+1):
    n = int(input())
    wood = input().split()
    wood = list(map(int, wood))
    wood.sort(reverse=True)
    print(fun(wood))

