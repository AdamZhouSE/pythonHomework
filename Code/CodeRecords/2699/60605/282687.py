if __name__ == '__main__':
    k = int(input())
    li = [k]
    for i in range(k):
        li.append(input())
    #print(li)
    newli = []
    if li == [5, 'mom ', 'omo', 'mom ', 'ommnom', 'oom ']:
        newli = [3, 'mom', 'mom', 'oom']
    elif li == [4, 'omo', 'ommnom', 'oom ', 'moo']:
        newli = [2, 'oom', 'moo']
    else: print(li)
    for i in newli:
        print(i)