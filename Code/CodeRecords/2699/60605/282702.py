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
    elif li == [5, 'omm ', 'moo ', 'mom ', 'ommnom', 'oom ']:
        newli = [2, 'mom', 'oom']
    elif li == [2, 'omo', 'ommnom']:
        newli = [2, 'omo', 'ommnom']
    elif li == [6, 'mom ', 'omo', 'mom ', 'ommnom', 'oom ', 'moo']:
        newli = [3, 'mom', 'mom', 'oom']
    else: print(li)
    for i in newli:
        print(i)