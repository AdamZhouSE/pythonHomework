def absenceAndRepetition():
    input()
    out = ""
    list = [int(i) for i in input().split()]
    array = [1 for i in range(len(list))]
    for i in range(len(list)):
        array[list[i]-1] = array[list[i]-1]-1
    if(array.count(-1)>0):
        out=out+str(array.index(-1)+1)+' '
    else:
        out = out + "0 "
    if(array.count(1)>0):
        out = out + str(array.index(1) + 1)
    else:
        out = out + "0"
    print(out)

times = int(input())
for i in range(times):
    absenceAndRepetition()