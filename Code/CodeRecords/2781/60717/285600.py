count=1
while True:
    try:
        list1=[]
        x=input()
        while x!='9':
            list1.append(x)
            x=input()
        flag=0
        for i in range(0,len(list1)-1):
            for j in range(i+1,len(list1)):
                if len(list1[i]) >= len(list1[j]):
                    if list1[i][:len(list1[j])]==list1[j]:
                        flag=1
                elif len(list1[i]) <= len(list1[j]):
                    if list1[j][:len(list1[i])]==list1[i]:
                        flag=1
        if flag==0:
            print('Set '+str(count)+' is immediately decodable')
        else:
            print('Set '+str(count)+' is not immediately decodable')
        count+=1
    except:
        break