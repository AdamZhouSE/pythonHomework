count=1
while True:
    try:
        list1=[]
        x=input()
        while x!='9':
            list1.append(input())
            x=input()
        flag=0
        for i in range(0,len(list1)-1):
            for j in range(i+1,len(list1)):
                if list1[i]in list1[j] or list1[j] in list1[i]:
                    flag=1
        if flag==1:
            print('Set '+str(count)+' is immediately decodable')
        else:
            print('Set '+str(count)+' is not immediately decodable')
        count+=1
    except:
        break