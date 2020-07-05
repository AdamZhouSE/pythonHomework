L = int(input())
source = input()
source1 = source
lists = []
lists1 = []
listlen = []
for a in range(0,L):
    word = input()
    lists.append(word)
    lists1.append(word)
    listlen.append(len(word))
count = 0
while source!="":
    if count==2:    
        print(source1)
        print([x for x in lists1])
        print(source)
        print([x for x in lists])
        print([x for x in listlen])
    index = listlen.index(max(listlen))
    count = count + source.count(lists[index])
    source = source.replace(lists[index],"",source.count(lists[index]))
    del lists[index]
    del listlen[index]
print(count)


