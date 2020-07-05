def operation(string):
    num=0
    substr=[]
    numbers=[]
    for i in range(len(string)-2):
        for j in range(i+2,len(string)):
            substr.append(string[i:j+1])
    substr=set(substr)
    substr=[[j for j in i] for i in substr]
    type=[]
    for i in substr:
        count0 = i.count('0')
        count1 = i.count('1')
        count2 = i.count('2')
        if [count0,count1,count2] in numbers and count0==1 :
            num+=1
            if [count0,count1,count2] not in type:
                 type.append([count0,count1,count2])
        numbers.append([count0,count1,count2])
    return num+len(type)

t=int(input())
for i in range(t):
    string=input()
    print(operation(string))