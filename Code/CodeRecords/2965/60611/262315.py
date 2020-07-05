l = []
l.append(input())
l.append(input())
num = int(input())
for i in range(num):
    l.append(input())
need = list(map(int, l[0].split()))


def copypaste(list1, str1):
    insert = str1[list1[0] : list1[1]]
    length=len(str1)
    result=str1[:list1[2]] + insert + str1[list1[2]:]
    l[1]=result


for i in range(num):
    tmp=list(map(int,l[i+2].split()))
    copypaste(tmp,l[1])
    print(l[1])
print(l[1][:need[0]])
