num = int(input())
st = []
pa = []
for i in range(num):
    st.append(list(input()))
    pa.append(list(input()))
for i in range(num):
    index = len(st[i])
    for j in range(len(pa[i])):
        for k in range(len(st[i])):
            if pa[i][j] == st[i][k]:
                if index > k:
                    index = k
                break
    if index == len(st[i]):
        print("$")
    else:
        print(st[i][index])