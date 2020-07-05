problems = int(input())
for x in range(problems):
    list = [0 for x in range(int(input()))]
    temp = input().split(" ")
    for x in range(len(temp)):
        list[x] = int(temp[x])
    
    count = 0
    i = 0
    while i < len(list) - 2:
        j = i + 1
        while j < len(list) - 1:
            k = j + 1
            while k < len(list):
                if (list[i]+list[j]>list[k])and(list[i]+list[k]>list[j])and(list[k]+list[j]>list[i]):
                    count += 1
                k += 1
            j += 1
        i += 1
    print(count)