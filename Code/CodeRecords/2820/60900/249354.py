n = input()
List = []
for i in range(0,(int)(n)):
    List.append(input())
print(1+len(List)-len(list(set(List))))