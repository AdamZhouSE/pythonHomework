total = int(input())
data = []
for i in range(0,total):
    ls = input()
    data.append(ls)
for i in range(0,total):
    ss = list(set(data[i]))
    if len(ss)%2==1:
        print("HE!")
    else:
        print("SHE!")
    