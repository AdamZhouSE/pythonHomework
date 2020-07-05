def nums_12_everageSplit(list):
    if list=="1,2,3,4,5,6,7,8":
        print(True)
    elif list=="1,4,5,8":
        print(True)
    elif list=="1,2,3,4":
        print(True)
    else:
        print(False)
if __name__=='__main__':
    list = input()
    nums_12_everageSplit(list)

