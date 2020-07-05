arr = input()[2:-2]
arr2 = input()[1:-1]
temp = [j.split(',') for j in [i for i in arr.split('],[')]]
sections = [[]]
for i in range(len(temp)):
    sections.append([int(j) for j in temp[i]])
sections.pop(0)
newSection = [int(i) for i in arr2.split(',')]

for i in range(len(sections)):
    if (sections[i][0]<=newSection[0]) and (i+1)<len(sections):
        continue
    else:
        sections.insert(i, newSection)
        if i>=1 and sections[i-1][1]>=sections[i][0]:
            sections[i-1] = [sections[i-1][0], sections[i][1]]
            while i<len(sections)-1 and sections[i][1]>=sections[i+1][0]:
                sections[i-1] = [sections[i-1][0], max(sections[i+1][1],sections[i][1])]
                sections.pop(i+1)
            sections.pop(i)
            break
        elif i+1<len(sections) and sections[i][1]>=sections[i+1][0]:
            sections[i+1] = [sections[i][0], sections[i+1][1]]
            sections.pop(i)
            break
        else:
            break
print(sections)