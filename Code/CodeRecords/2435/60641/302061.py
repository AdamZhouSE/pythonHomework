num_of_words, num_of_questions = map(int,input().split(" "))
words = []
questions = []
for i in range(0, num_of_words):
    words.append(input())
for i in range(0, num_of_questions):
    lower, upper = map(int, input().split(" "))
    lower = lower - 1
    temp = sorted(words[lower:upper],reverse=True)
    print(temp[0])
