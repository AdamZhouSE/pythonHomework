import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

def mul(number):
    answer = 1
    for i in range(1,number+1):
        answer *= i
    return answer

n = int(lst[0])
k = int(lst[1]) - 1

wordsList = []
for i in range(1,n+1):
    wordsList.append(i)

answer = ''
while n > 0:

    No = int(k / mul(n-1) )
    k = k % mul(n-1)
    answer += str(wordsList[No])
    wordsList.remove(wordsList[No])
    n -= 1
print(answer)
