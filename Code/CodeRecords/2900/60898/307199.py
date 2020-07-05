def strings_13_count(strings):
    strings = strings.replace(' ','')
    print(len(strings),end='')
if __name__=='__main__':
    strings = input()
    strings_13_count(strings)