n = int(input())
result=[]

for i in range(n):
    list_len=int(input())
    l=input().split(" ")    #输入的list
    m=int(input())    #要删除的个数

    number_of_element=[]
    while len(l)>0:
        num = int(1)  # 第0个元素的个数
        j=1
        while j<len(l):
            if l[j]==l[0]:
                num=num+1
                del l[j]
            else:
                j=j+1
        del l[0]
        number_of_element.append(num)

    while m>0:
       if m>=min(number_of_element):
           m=m-min(number_of_element)
           del number_of_element[number_of_element.index(min(number_of_element))]

    result.append(len(number_of_element))

for i in range(len(result)):
    print(result[i])