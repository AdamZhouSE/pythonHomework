def sort_0(source):
    source_char=list(map(int,source.split('+')))
    source_char.sort()
    result=''
    for num in source_char:
        result=result+str(num)+'+'
    print(result[:-1])
source=input("")
sort_0(source)