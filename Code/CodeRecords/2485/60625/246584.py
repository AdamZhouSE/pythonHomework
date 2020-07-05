num = int(input())
for i in range(num):
    Num=int(input())
    List=input().split()
    List_of_element=[]
    for n in range(Num):
        Consist_of_element = list(List[n])
        Consist_of_element.sort()
        List_of_element.append(''.join(Consist_of_element))
        for element in List:
            elementConsist=list(element)
            elementConsist.sort()
            if elementConsist!=Consist_of_element:
                List_of_element.append(''.join(elementConsist))
    List_of_element=list(set(List_of_element))

    Index_of_element = []
    for index in range(len(List_of_element)):
        Consist_of_element = list(List_of_element[index])
        Consist_of_element.sort()
        Index_of_element.append(0)
        for element in List:
            elementConsist=list(element)
            elementConsist.sort()
            if elementConsist == Consist_of_element:
                Index_of_element[index]=Index_of_element[index]+1

    for j in range(len(Index_of_element)):
        for l in range(len(Index_of_element) - 1):
            if Index_of_element[l] > Index_of_element[l + 1]:
                temp = Index_of_element[l]
                Index_of_element[l] = Index_of_element[l + 1]
                Index_of_element[l + 1] = temp
    print(' '.join(str(i) for i in Index_of_element))