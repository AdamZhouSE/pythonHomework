dict={}
record={}    # 最后一次的成绩是在第几次
time=int(input())
for i in range(0,time):
    string=input()
    name=string.split(" ")[0]
    score=int(string.split(" ")[1])
    num=dict.get(name)
    if num==None:
        dict[name]=score
        record[name]=[str(score)+"&"+str(i)]
    else:
        dict[name]=num+score
        record[name].append(str(score)+"&"+str(i))


most=max(dict.values())
arr=list(filter(lambda x:dict[x] == most, dict))
array=[]
if len(arr)==1:
    print(arr[0])
else:
    for item in arr:
        tempList=record.get(item)
        sum=0
        for num in tempList:
            sum+=int(num.split("&")[0])
            if sum>=most:
                array.append(int(num.split("&")[1]))
                break
smallest=min(array)
index=array.index(smallest)
print(arr[index])