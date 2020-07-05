List = input()
Data = []
for n in range(0, len(List), 2):
    Data.append(List[n])
Data.sort()
res = ""
for i in range(0, len(Data) - 1):
    res += Data[i]
    res += "+"
res += Data[len(Data) - 1]
print(res)