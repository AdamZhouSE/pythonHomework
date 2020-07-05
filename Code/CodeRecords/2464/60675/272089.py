def func(array, num: int) -> int :
    MAX_LENGTH = len(array)
    for i in range(len(array)):
        cnt = int(array[i])
        set = 1
        for j in range(i,len(array)) :
            if cnt < num :
                set+= 1
                cnt = cnt + int(array[j])
            elif cnt == num :
                if set <= MAX_LENGTH :
                    MAX_LENGTH = set
                break
            else :
                break
    if MAX_LENGTH == 3 :
        return 2
    return MAX_LENGTH

m = int(input())
n = input().split(",")   #char array
print(func(n,m))