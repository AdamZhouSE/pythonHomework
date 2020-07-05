num = int(input())
result = "A"


def help(times, string):
    return string + chr(ord('A')+times) + string

for i in range(1,num):
    result = help(i,result)
print(result)
