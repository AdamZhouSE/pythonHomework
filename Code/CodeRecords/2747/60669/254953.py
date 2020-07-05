def init():
    copy=arr.copy()
    record={}

    for item in arr:
        if item==end:
            break
        for word in copy:
            if item==word:
                continue
            diff=0
            list1=list(item)
            list2=list(word)
            for char in list1:
                if list2.count(char)==0:
                    diff+=1
            if diff==1:
                if record.get(item)==None:
                    record[item]=[word]
                else:
                    record[item].append(word)
    return record

def find():
    word=begin
    tempList=[]
    tempList.append(word)
    while word!=end:
        value=record.get(word)
        if len(value)==1:
            tempList.append(value[0])
        else:      # len(value)>1
            if end in value:
                tempList.append(end)
                break
            tempValue=value.copy()
            for x in value:
                if x in tempList:
                    tempValue.remove(x)
            value=tempValue.copy()

            hasEnd = False
            hasEndList = []
            for x in value:
                if end in record.get(x):
                    hasEnd = True
                    hasEndList.append(x)
            if hasEnd:
                value=hasEndList

            for item in value:
                repetition = False
                if result==[]:
                    tempList.append(item)
                    break
                else:
                    for arr in result:
                        if len(tempList)>1 and arr[len(tempList)-1]==tempList[-1] and  arr[len(tempList)]==item:
                            repetition=True
                            break
                    if repetition==False:
                        tempList.append(item)
                        break
                    else:
                        if value.index(item)==len(value)-1:
                            return None
        if word not in tempList:
            word=tempList[-1]
        else:
            return None
    return tempList

if __name__ == '__main__':
    begin = input()
    end = input()
    arr = eval(input())
    arr.insert(0,begin)
    result=[]
    record=init()

    while True:
        temp=find()
        if temp!=None:
            result.append(temp)
        else:
            break
    print(result)
