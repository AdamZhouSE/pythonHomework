def func(source:str):

    if source.find('-')>0:
        return 'True'
    try:
        res = int(source)
        return ('True')
    except :
        return ('False')
source=input()
print(func(source))