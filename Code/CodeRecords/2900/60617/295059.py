import re
def titleLen():
    title=input()
    title=re.split('\s',title)
    title="".join(title)
    print(len(title))

if __name__=='__main__':
    titleLen()