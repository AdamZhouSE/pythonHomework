null = 0
def find(index,a):
    if(a[index] == 0):
        return 0
    else:
        if((index+1)*2-1 >= len(a)):
            return 1
        else:
            x = find((index+1)*2-1,a)+1
            y = find((index+1)*2,a) + 1
            return min(x,y)
a = eval(input())
print(find(0,a))