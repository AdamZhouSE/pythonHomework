def solve(list):
    i=0
    for num in list:
        i^=num
    return i
list=input().split(',')
list[0]=(list[0]).split('[')[1]
list[len(list) - 1]=list[len(list) - 1].split(']')[0]
list=[int(i) for i in list]
print(solve(list))
