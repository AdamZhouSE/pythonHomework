l = input()
l = l.replace('[', '')
l = l.replace(']', '')
l = l.split(',')
l = [int(x) for x in l]

k = int(input())

dis = []
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        dis.append(abs(l[j] - l[i]))

dis.sort()
print(dis[k - 1])