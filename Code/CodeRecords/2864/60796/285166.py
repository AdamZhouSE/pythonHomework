def bubble():
    for i in range(len(numbers)-1):
        j=0
        while j<len(numbers)-i-1:
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
                time[j],time[j+1]=time[j+1],time[j]
            j=j+1
def build(before,have_selected):#before:前面选的数的下标,have_selected：已经选的数
    #没有可选的了
    if before>=len(this_set):
        sum=0
        for i in range(len(have_selected)):
            n=have_selected[i]
            sum=sum+n*time[numbers.index(n)]
        if sum>this_result[0]:
            this_result[0]=sum
        return
    #隔一个选
    build(before+2,have_selected+[this_set[before]])
    #隔两个选
    if before+2<len(this_set):
        build(before + 3, have_selected + [this_set[before]])


N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
numbers=[]
time=[]
for i in range(N):
    now=ls[i]
    if not numbers.__contains__(now):
        numbers.append(now)
        time.append(1)
    else:
        ind=numbers.index(now)
        time[ind]=time[ind]+1
bubble()
number_set=[[numbers[0]]]
for i in range(1,len(numbers)):
    now=numbers[i]
    if number_set[len(number_set)-1].__contains__(now-1):
        number_set[len(number_set)-1].append(now)
    else:
        number_set.append([now])
result=0
i=0
while i<len(number_set):
    this_set=number_set[i]
    #第一个要么选要么不选
    #选了一个后要么隔一个再选，要么隔两个再选
    if len(this_set)==1:
        result=result+this_set[0]*time[numbers.index(this_set[0])]
        i=i+1
        continue
    if len(this_set)==2:
        if this_set[0]*time[numbers.index(this_set[0])]>this_set[1]*time[numbers.index(this_set[1])]:
            result=result+this_set[0]*time[numbers.index(this_set[0])]
        else:
            result=result+this_set[1]*time[numbers.index(this_set[1])]
        i=i+1
        continue
    this_result=[0]
    build(0,[])#选第一个
    build(1,[])#选第二个
    result=result+this_result[0]
    i=i+1

print(result)




