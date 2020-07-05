count=int(input())
list1=[]
list2=[]

while count>0:  #count sub
    sum=0
    token=[i for i in input()]
    i=0
    end= False
    while i<len(token)-1:
        if token[i]=='(':
            if token[i+1]==')':
                i=i+1
                sum=sum+2
            else:
                end=True
        else:
            end=True

        i=i+1
        if end or i>=len(token)-1:
            end=False
            list1.append(sum)
            sum=0

    list2.append(max(list1))
    count=count-1

for i in list2:
    print(i)