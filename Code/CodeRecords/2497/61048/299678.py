def sort7():
    target=int(input())
    str1=input()
    str2=input()
    position=[int(x) for x in str1[1:len(str1)-1].split(',')]
    speed=[int(x) for x in str2[1:len(str2)-1].split(',')]

    lst = sorted(zip(position, speed))
    set=[]
    for p, s in lst:
        set.append((target-p)/s)
    res = 0
    head=0
    while len(set) >= 1:
        if(len(set)==1):
            if(head!=set[0]):
                res+=1
            break
        head = set.pop()
        if head < set[-1]:
            res += 1
        else:
            set[-1] = head
    print(res)
    return

sort7()def sort1():
    a = input()
    list1 =sorted(a[1:len(a) - 1].split(','))
    number = [int(x) for x in list1]

    return number
list=sort1()
print(list)