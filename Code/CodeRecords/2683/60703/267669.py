T = int(input())
for m in range(T):
    Str = input()
    length = len(Str)
    max = 0
    for i in range(0,length):
        temp = 0
        for j in range(i+1,length):
            if(Str[j]<=Str[j-1]):
                break
            else:
                temp+=1
        if(temp>max):
            max = temp
    print(max)