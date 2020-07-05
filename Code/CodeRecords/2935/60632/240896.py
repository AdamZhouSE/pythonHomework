s = input()
data = []
for i in s:
    if i == 'Q' or i == 'A':
        data.append(i)
count = 0
for i in range(len(data)-2):
    if data[i] == 'Q':
        for j in range(i+1, len(data)-1):
            if data[j] == 'A':
                for k in range(j+1, len(data)):
                    if data[k] == 'Q':
                        count += 1
print(count,end='')
