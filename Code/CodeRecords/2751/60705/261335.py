if __name__ == '__main__':
    matrix = []
    line = input()
    while line != "":
        matrix.append(line.split(" "))
        try:
            line = input()
        finally:
            print(matrix)
