num_of_sentence = int(input())
sentence = [[]]
for i in range(0, num_of_sentence):
    sentence.append(input().split(" "))
num_of_question = int(input())
for i in range(0, num_of_question):
    word = input()
    result = []
    for j in range(1, len(result)):
        if word in result[j]:
            result.append(str(j))
    if len(result) == 0:
        print(" ")
    else:
        print(" ".join(result) + " ")
