def sort_9_Union(list1=[],list2 = []):
    list1.sort()
    list2.sort()
    re = []
    i = j = 0
    while i<len(list1) and j<len(list2):
        if list1[i]==list2[j]:
            re.append(list1[i])
            i += 1
            j += 1
        elif list1[i]<list2[j]:
            i += 1
        else:
            j += 1
    print(re)
if __name__=='__main__':
    list1 = eval(input())
    list2 = eval(input())
    sort_9_Union(list1,list2)