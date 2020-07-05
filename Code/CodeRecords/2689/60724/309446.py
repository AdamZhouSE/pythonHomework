T=int(input())
for m in range(T):
    string=input().split(" ")
    string1=string[0]
    string2=string[1]
    set1=[]
    set2=[]
    for i in range(len(string1)):
        set1.append(string1[i])
    for i in range(len(string2)):
        set2.append(string2[i])
    allsubset=[]
    def subset(set,choice,i):
        if i==1:
            for j in range(len(choice)):
                new_set=set[:]
                new_set.append(choice[j])
                allsubset.append(new_set)
        else:
            for j in range(len(choice)-i+1):
                new_set=set[:]
                new_set.append(choice[j])
                subset(new_set,choice[j+1:],i-1)
    for i in range(1,len(set1)+1):
        subset([],set1,i)
    set1=allsubset[:]
    allsubset=[]
    for i in range(1,len(set2)+1):
        subset([],set2,i)
    set2=allsubset[:]
    result=0
    for i in range(len(set1)):
        if set1[i] in set2:
            result=max(result,len(set1[i]))
    print(len(string1)+len(string2)-result)