List = input()
List = List[1:len(List)-1]
List = List.split(",")

for i in range(len(List)):
    List[i] = int(List[i])
big = 0
for i in range(len(List)):
    tmp = List[i]
    j = i
    while j > 0 and List[j-1] > tmp:
        List[j] = List[j-1]
        j = j-1
    List[j] = tmp
print(List)