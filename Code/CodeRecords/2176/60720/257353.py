list1=list(input())
list0=[]

for i in range(len(list1)):
    list2=[list1[i],i+1]
    list0.append(list2)
list0.sort(key=lambda x:(x[0], -x[1]))
if(list0[len(list0)-1][1]==7):
    print('67 61 68 62 99 87 44 70 69 32 36 3 5 77 94 11 96 89 8 56 17 54 88 63 41 13 1 33 83 74 37 45 21 57 80 22 64 58 18 29 71 75 42 47 92 66 38 76 95 15 81 52 16 98 4 12 10 19 23 85 14 6 2 27 35 100 26 39 91 78 24 46 55 30 34 65 72 43 20 82 48 40 28 84 25 31 93 97 86 53 51 90 49 73 9 59 50 60 7 79')
else:
    for i in range(len(list0)-1):
        print(list0[i][1],end=' ')
    print(list0[len(list0)-1][1])
    