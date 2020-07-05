def Test():
    num=eval(input())
    groups=[]
    for i in range(0,20):
        groups.append([])
    for numbers in num:
        for j in range(0,len(groups)):
            if(not(groups[j])):
                groups[j].append(numbers)
                break
            else:
                if(numbers<groups[j][-1]):
                    groups[j].append(numbers)
                    break
    count=0
    for list in groups:
        if(list):
            count=count+1
    print(count)
if __name__ == "__main__":
    Test()