li = []
count = 1

try:
    while True:
        s = input()
        if s != '9':
            li.append(s)
        else:
            ans = 0
            for i in range(len(li) - 1):
                for j in range(i+1, len(li)):
                    if len(li[j]) > len(li[i]):
                        if li[i] == li[j][:len(li[i])]:
                            ans = 1
                    elif len(li[j]) <= len(li[i]):
                        if li[j] == li[i][:len(li[j])]:
                            ans = 1
            if ans == 1:
                print('Set %d is not immediately decodable' %count)
            else:
                print('Set %d is immediately decodable' %count)
            count+=1
            li.clear()
except EOFError:
    pass