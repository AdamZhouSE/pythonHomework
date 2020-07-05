stopWord = ']'
image = ''
for line in iter(input, stopWord):
    image += line + '\n'
image += ']\n'
init=eval(image)
class Dsu():
    elements=[]
    valid=True
    def __init__(self,initialElement):
        self.elements=initialElement
class Element():
    dsu=None
    content=[]
all=[]
allDsu=[]
for i in range(len(init)):
    for j in range(len(init)):
        for k in range(4):
            temp1=Element()
            temp2=Dsu([])
            temp1.content=[i,j,k]
            temp2.elements.append(temp1)
            temp1.dsu=temp2
            all.append(temp1)
            allDsu.append(temp2)
for i in range(len(init)):
    for j in range(len(init)):
        if init[i][j]=='/':
            all[(i * len(init) + j) * 4 + 1].dsu.valid=False
            all[(i * len(init) + j) * 4 + 3].dsu.valid=False
            all[(i * len(init) + j) * 4].dsu.elements = all[(i* len(init) + j) * 4].dsu.elements + all[(i * len(init) + j) * 4 + 1].dsu.elements
            for k in all[(i * len(init) + j) * 4 + 1].dsu.elements:
                k.dsu=all[(i * len(init) + j) * 4].dsu
            all[(i * len(init) + j) * 4+2].dsu.elements = all[(i* len(init) + j) * 4+2].dsu.elements + all[(i * len(init) + j) * 4 + 3].dsu.elements
            for k in all[(i * len(init) + j) * 4 + 3].dsu.elements:
                k.dsu=all[(i * len(init) + j) * 4+2].dsu
        elif init[i][j]=='\\':
            all[(i * len(init) + j) * 4 + 2].dsu.valid=False
            all[(i * len(init) + j) * 4 + 3].dsu.valid=False
            all[(i * len(init) + j) * 4].dsu.elements = all[(i* len(init) + j) * 4].dsu.elements + all[(i * len(init) + j) * 4 + 3].dsu.elements
            for k in all[(i * len(init) + j) * 4 + 3].dsu.elements:
                k.dsu=all[(i * len(init) + j) * 4].dsu
            all[(i * len(init) + j) * 4+1].dsu.elements = all[(i* len(init) + j) * 4+1].dsu.elements + all[(i * len(init) + j) * 4 + 2].dsu.elements
            for k in all[(i * len(init) + j) * 4 + 2].dsu.elements:
                k.dsu=all[(i * len(init) + j) * 4+1].dsu
        else:
            for k in range(1,4):
                all[(i * len(init) + j) * 4 + k].dsu.valid=False
                all[(i * len(init) + j) * 4].dsu.elements = all[(i * len(init) + j) * 4].dsu.elements + all[(i * len(init) + j) * 4 + k].dsu.elements
                for l in all[(i * len(init) + j) * 4 + k].dsu.elements:
                    l.dsu = all[(i * len(init) + j) * 4].dsu
for i in range(len(init)):
    for j in range(len(init)):
        if j!=len(init)-1 and all[(i * len(init) + j) * 4 + 3] not in all[(i * len(init) + j+1) * 4+1].dsu.elements:
            all[(i * len(init) + j) * 4 + 3].dsu.valid = False
            all[(i * len(init) + j+1) * 4+1].dsu.elements=all[(i * len(init) + j+1) * 4+1].dsu.elements+all[(i * len(init) + j) * 4 + 3].dsu.elements
            for k in all[(i * len(init) + j) * 4 + 3].dsu.elements:
                k.dsu=all[(i * len(init)+j+1) * 4+1].dsu
        if i!=len(init)-1 and all[(i * len(init) + j) * 4 + 2] not in all[((i+1) * len(init) + j) * 4].dsu.elements:
            all[(i * len(init) + j) * 4 + 2].dsu.valid = False
            all[((i+1) * len(init) + j) * 4].dsu.elements=all[((i+1) * len(init) + j) * 4].dsu.elements+all[(i * len(init) + j) * 4+2].dsu.elements
            for k in all[(i * len(init) + j) * 4 + 2].dsu.elements:
                k.dsu = all[((i+1) * len(init) + j) * 4].dsu
count=0
for i in allDsu:
    if i.valid:
        count+=1
print(count)