def sort1():
    a = input()
    list1 =sorted(a[1:len(a) - 1].split(','))
    number = [int(x) for x in list1]

    return number
list=sort1()
print(list)