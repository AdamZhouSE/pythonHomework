words = int(input())
letter = input()
lst = []
for l in range(words):
    list.append(lst, input())
lst.sort(key=lambda x: len(x), reverse=True)
pointer = 0
index = 0
count = 0
for overlap in range(len(letter)):
    while len(letter) - pointer + overlap < len(lst[index]):
        index = (index + 1) % words

    while True:
        if letter[pointer - overlap:].startswith(lst[index]):
            pointer = pointer + len(lst[index]) - overlap
            count = count+1
        index = (index + 1) % words
        if index == 0:
            break
    if pointer == len(letter)-1:
        break
print(count)